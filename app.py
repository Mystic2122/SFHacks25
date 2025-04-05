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


# Route for the homepage (Login/Signup page)
@app.route("/")
def index():
    return render_template("index.html")


# Route to display the game (after user login)
@app.route("/game/<userId>")
def game(userId):
    player = random.choice(list(players.find()))  # Randomly selects a player

    # Initialize the user's score if it's their first time
    if userId not in user_scores:
        user_scores[userId] = 0

    return render_template(
        "game.html",
        userId=userId,
        player=player,
        score=user_scores[userId],
        player_data=player,
    )


# Route to handle the guess submission
@app.route("/guess", methods=["POST"])
def guess():
    userId = request.form["userId"]
    user_guess = request.form["guess"]
    player_name = request.form["player_name"]  # The actual player to guess

    if user_guess.lower() == player_name.lower():
        # Correct guess - add 1 point
        user_scores[userId] += 1
        result = "correct"
        # Get a new player for the next round
        new_player = random.choice(list(players.find()))
        return jsonify(
            {
                "result": result,
                "score": user_scores[userId],
                "new_player": {
                    "name": new_player["name"],
                    "blured_img": new_player["blured_img"],
                },
            }
        )
    else:
        # Incorrect guess - reset the score
        user_scores[userId] = 0
        result = "incorrect"
        return jsonify({"result": result, "score": user_scores[userId]})


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

<script>
  const guessInput = document.getElementById("guess");
  const autocompleteList = document.createElement("ul");
  autocompleteList.style.position = "absolute";
  autocompleteList.style.backgroundColor = "white";
  autocompleteList.style.border = "1px solid #ccc";
  autocompleteList.style.listStyleType = "none";
  autocompleteList.style.padding = "0";
  autocompleteList.style.margin = "0";
  autocompleteList.style.width = guessInput.offsetWidth + "px";
  autocompleteList.style.zIndex = "1000";
  autocompleteList.style.display = "none";
  document.body.appendChild(autocompleteList);

  guessInput.addEventListener("input", function () {
    const query = guessInput.value.trim();

    if (query.length === 0) {
      autocompleteList.style.display = "none";
      return;
    }

    fetch(`/autocomplete?q=${encodeURIComponent(query)}`)
      .then((response) => response.json())
      .then((data) => {
        autocompleteList.innerHTML = ""; // Clear previous suggestions
        if (data.length === 0) {
          autocompleteList.style.display = "none";
          return;
        }

        data.forEach((name) => {
          const listItem = document.createElement("li");
          listItem.textContent = name;
          listItem.style.padding = "5px";
          listItem.style.cursor = "pointer";

          listItem.addEventListener("click", function () {
            guessInput.value = name; // Set the input value to the selected name
            autocompleteList.style.display = "none"; // Hide the dropdown
          });

          autocompleteList.appendChild(listItem);
        });

        const rect = guessInput.getBoundingClientRect();
        autocompleteList.style.top = rect.bottom + window.scrollY + "px";
        autocompleteList.style.left = rect.left + window.scrollX + "px";
        autocompleteList.style.display = "block";
      })
      .catch((error) => {
        console.error("Autocomplete error:", error);
        autocompleteList.style.display = "none";
      });
  });

  // Hide the dropdown when clicking outside
  document.addEventListener("click", function (event) {
    if (!guessInput.contains(event.target) && !autocompleteList.contains(event.target)) {
      autocompleteList.style.display = "none";
    }
  });
</script>
