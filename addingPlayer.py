from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")

s = f"mongodb+srv://{username}:{password}@sfhacks25.ahebnig.mongodb.net/"

client = MongoClient(s)

# Select the database (if the database does not exist, MongoDB will create it)
db = client.sports  # "sports" is the database name

# Select the collection (if the collection does not exist, MongoDB will create it)
players = db.players  # "players" is the collection name

# Example player data
player_data = {
    "name": "LeBron James",
    "teams": ["Cleveland Cavaliers", "Miami Heat", "Los Angeles Lakers"],
    "championships": 4,
    "position": "Forward",
    "years_active": [2003, 2023],
}

# Insert the player data into the collection
result = players.insert_one(player_data)

print(f"Player added with ID: {result.inserted_id}")
