# filepath: c:\Code\SFHacks25\test_mongodb_connection.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")

s = f"mongodb+srv://{username}:{password}@sfhacks25.ahebnig.mongodb.net/"

try:
    client = MongoClient(s)
    client.admin.command("ping")
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
