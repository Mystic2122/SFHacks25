from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve MongoDB credentials from environment variables
username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")

# Construct MongoDB connection string using credentials
uri = f"mongodb+srv://{username}:{password}@sfhacks25.ahebnig.mongodb.net/"

# Establish a connection to MongoDB
client = MongoClient(uri)

# Select the database and collection
db = client.sports  # Ensure this matches your actual database name
db.players.drop()  # Ensure this matches your actual collection name

# Delete a player document where the name is "Jaren Jackson Jr."
