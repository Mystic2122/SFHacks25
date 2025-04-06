from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import random

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Get MongoDB credentials from environment variables
mongodb_username = os.getenv("MONGODB_USERNAME")
mongodb_password = os.getenv("MONGODB_PASSWORD")

# Construct the MongoDB connection string
mongo_uri = f"mongodb+srv://{mongodb_username}:{mongodb_password}@sfhacks25.ahebnig.mongodb.net/"

# MongoDB connection setup
client = MongoClient(mongo_uri)
db = client.sports
players = db.players
user_list = db.users

# Initialize the user's score (in-memory for simplicity)
user_scores = {}
incorrect_guesses = {}  # Store incorrect guess counts


# Route for the homepage (Login/Signup page)
@app.route("/")
def index():
    return render_template("index.html")


# Route to display the game (after user login)
@app.route("/game/<userId>")
def game(userId):
    player = random.choice(list(players.find()))  # Randomly selects a player

    # Get the user's high score from the database
    user = user_list.find_one({"Userid": userId})
    if user:
        high_score = user.get("HighScore", 0)  # Default to 0 if not found
    else:
        high_score = 0  # Default to 0 if user not found
        # If user doesn't exist, create a new user entry with default high score
        user_list.insert_one({"Userid": userId, "HighScore": 0})

    # Initialize the user's score if it's their first time
    if userId not in user_scores:
        user_scores[userId] = 0
        incorrect_guesses[userId] = 0  # Initialize incorrect guesses

    return render_template(
        "game.html",
        userId=userId,
        player=player,
        score=user_scores[userId],
        high_score=high_score,  # Pass the high score to the template
        player_data=player,
    )


# Route to handle the guess submission
def get_initials(name):
    # Split the name into words and take the first letter of each word
    words = name.split()
    initials = "".join([word[0].upper() for word in words])
    return initials


@app.route("/guess", methods=["POST"])
def guess():
    userId = request.form["userId"]
    user_guess = request.form["guess"]
    player_name = request.form["player_name"]  # The actual player to guess

    if get_initials(user_guess).lower() == get_initials(player_name).lower():
        user_scores[userId] += 1
        incorrect_guesses[userId] = 0  # Reset incorrect guesses
        result = "correct"

        # Get the unblurred image
        correct_player = players.find_one({"name": player_name})
        unblured_img = correct_player.get("unblured_img", "")

        # Get the user's current high score from the database
        user = user_list.find_one({"Userid": userId})
        if user:
            old_high_score = user.get("HighScore", 0)
        else:
            old_high_score = 0

        # Check if the current score is greater than the old high score
        if user_scores[userId] > old_high_score:
            # Update the user's high score in the database
            user_list.update_one(
                {"Userid": userId}, {"$set": {"HighScore": user_scores[userId]}}
            )

        return jsonify(
            {
                "result": result,
                "score": user_scores[userId],
                "full_name": player_name,
                "unblured_img": unblured_img,
            }
        )
    else:
        # Incorrect guess
        incorrect_guesses[userId] = incorrect_guesses.get(userId, 0) + 1
        result = "incorrect"
        player = players.find_one({"name": player_name})
        height = player.get("height", "Unknown")  # Get height, default to "Unknown"
        teams = player.get("teams", [])  # Get teams, default to empty list

        if incorrect_guesses[userId] >= 3:
            # Get the user's high score from the database
            user = user_list.find_one({"Userid": userId})
            if user:
                high_score = user.get("HighScore", 0)
            else:
                high_score = 0

            # Reset user's score and incorrect guesses
            current_score = user_scores.get(userId, 0)

            # Get the user's current high score from the database
            user = user_list.find_one({"Userid": userId})
            if user:
                old_high_score = user.get("HighScore", 0)
            else:
                old_high_score = 0

            # Check if the current score is greater than the old high score
            if current_score > old_high_score:
                # Update the user's high score in the database
                user_list.update_one(
                    {"Userid": userId}, {"$set": {"HighScore": current_score}}
                )
                high_score = current_score  # Update high_score to the new value

            user_scores[userId] = 0
            incorrect_guesses[userId] = 0

            # Get the unblured image
            correct_player = players.find_one({"name": player_name})
            if correct_player:
                unblured_img = correct_player.get("unblured_img", "")
            else:
                unblured_img = ""

            return jsonify(
                {
                    "result": "game_over",
                    "current_score": current_score,
                    "high_score": high_score,
                    "correct_name": player_name,  # Send the correct name
                    "unblured_img": unblured_img,  # Send the unblurred image URL
                }
            )
        elif incorrect_guesses[userId] == 2:
            return jsonify(
                {
                    "result": result,
                    "score": user_scores[userId],
                    "height": height,
                    "teams": teams,
                    "show_info": True,  # Flag to show info
                }
            )
        else:
            return jsonify(
                {
                    "result": result,
                    "score": user_scores[userId],
                    "height": height,
                    "show_info": False,  # Flag to not show info
                }
            )


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Check if user exists with given username and password
    user = user_list.find_one({"Username": username, "Password": password})

    if user:
        # Redirect to the game page with the user's unique userId
        return jsonify({"redirect": url_for("game", userId=user["Userid"])})
    else:
        # If login fails, show an error message
        return jsonify({"error": "Invalid username or password"}), 400


@app.route("/autocomplete", methods=["GET"])
def autocomplete():
    query = request.args.get("q", "").lower()  # Get the query from the request
    if not query:
        return jsonify([])  # Return an empty list if no query is provided

    # Find player names that start with the query (case-insensitive)
    matching_players = players.find({"name": {"$regex": f"^{query}", "$options": "i"}})
    player_names = [player["name"] for player in matching_players]

    return jsonify(player_names)  # Return the list of matching player names


if __name__ == "__main__":
    app.run(debug=True)