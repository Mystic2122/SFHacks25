from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")

s = f"mongodb+srv://{username}:{password}@sfhacks25.ahebnig.mongodb.net/"

client = MongoClient(s)
try:
    client.admin.command("ping")
    print("success")
except Exception as e:
    print(e)
