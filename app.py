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
users = db.users  # Changed user_list to users to reflect the combined collection

# Initialize the user's score (in-memory for simplicity)
user_scores = {}
incorrect_guesses = {}


# Route for the homepage (Login/Signup page)
@app.route("/")
def index():
    return render_template("index.html")


# Route to display the game (after user login)
@app.route("/game/<userId>")
def game(userId):
    player = random.choice(list(players.find()))

    # Get the user from the database
    user = users.find_one({"Userid": userId})
    if user:
        high_score = user.get("HighScore", 0)
    else:
        # If user doesn't exist, create a new user entry with default high score
        users.insert_one({"Userid": userId, "HighScore": 0})
        high_score = 0

    # Initialize the user's score if it's their first time
    if userId not in user_scores:
        user_scores[userId] = 0
        incorrect_guesses[userId] = 0

    return render_template(
        "game.html",
        userId=userId,
        player=player,
        score=user_scores[userId],
        high_score=high_score,
        player_data=player,
    )


# Route to handle the guess submission
def get_initials(name):
    words = name.split()
    initials = "".join([word[0].upper() for word in words])
    return initials


@app.route("/guess", methods=["POST"])
def guess():
    userId = request.form["userId"]
    user_guess = request.form["guess"]
    player_name = request.form["player_name"]

    if get_initials(user_guess).lower() == get_initials(player_name).lower():
        user_scores[userId] += 1
        incorrect_guesses[userId] = 0
        result = "correct"

        # Get the unblurred image
        correct_player = players.find_one({"name": player_name})
        unblured_img = correct_player.get("unblured_img", "")

        # Get the user's current high score from the database
        user = users.find_one({"Userid": userId})
        if user:
            old_high_score = user.get("HighScore", 0)
        else:
            old_high_score = 0

        # Check if the current score is greater than the old high score
        if user_scores[userId] > old_high_score:
            # Update the user's high score in the database
            users.update_one(
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
        height = player.get("height", "Unknown")
        teams = player.get("teams", [])

        if incorrect_guesses[userId] >= 3:
            # Get the user's high score from the database
            user = users.find_one({"Userid": userId})
            if user:
                high_score = user.get("HighScore", 0)
            else:
                high_score = 0

            # Reset user's score and incorrect guesses
            current_score = user_scores.get(userId, 0)

            # Get the user's current high score from the database
            user = users.find_one({"Userid": userId})
            if user:
                old_high_score = user.get("HighScore", 0)
            else:
                old_high_score = 0

            # Check if the current score is greater than the old high score
            if current_score > old_high_score:
                # Update the user's high score in the database
                users.update_one(
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
                    "correct_name": player_name,
                    "unblured_img": unblured_img,
                }
            )
        elif incorrect_guesses[userId] == 2:
            return jsonify(
                {
                    "result": result,
                    "score": user_scores[userId],
                    "height": height,
                    "teams": teams,
                    "show_info": True,
                }
            )
        else:
            return jsonify(
                {
                    "result": result,
                    "score": user_scores[userId],
                    "height": height,
                    "show_info": False,
                }
            )


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Check if user exists with given username and password
    user = users.find_one({"Username": username, "Password": password})

    if user:
        # Redirect to the game page with the user's unique userId
        return jsonify({"redirect": url_for("game", userId=user["Userid"])})
    else:
        # If login fails, show an error message
        return jsonify({"error": "Invalid username or password"}), 400


@app.route("/autocomplete", methods=["GET"])
def autocomplete():
    query = request.args.get("q", "").lower()
    if not query:
        return jsonify([])

    # Find player names that start with the query (case-insensitive)
    matching_players = players.find({"name": {"$regex": f"^{query}", "$options": "i"}})
    player_names = [player["name"] for player in matching_players]

    return jsonify(player_names)


@app.route("/signup", methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]

    # Check if the username already exists
    existing_user = users.find_one({"Username": username})
    if existing_user:
        return jsonify({"error": "Username already exists"}), 400

    # Create a new user document
    new_user = {
        "Username": username,
        "Password": password,
        "Userid": str(random.randint(100000, 999999)),  # Generate a unique Userid
        "HighScore": 0,  # Initialize high score to 0
    }

    # Insert the new user into the database
    users.insert_one(new_user)

    # Redirect to the login page or the game page
    return jsonify({"redirect": url_for("index")})  # Redirect to the login page


if __name__ == "__main__":
    app.run(debug=True)
