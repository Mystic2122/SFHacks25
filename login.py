from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("GAME_UN")
password = os.getenv("GAME_PW")

s = f"mongodb+srv://{username}:{password}@sfhacks25.ahebnig.mongodb.net/"

client = MongoClient(s)

db = client.sports

user_list = db.users

logged_in = False

while logged_in == False:
    command = input("Login or Signup: ")
    command = command.lower()
    if command == "login":
        username = input("Username: ")
        password = input("Password: ")
        if user_list.find_one({"Username": username, "Password": password}) != None:
            print("Succesful Login!")
            userId = user_list.find_one(
                {"Username": username, "Password": password}, {"Userid": 1, "_id": 0}
            )
            userId = userId["Userid"]
            logged_in = True
        else:
            print("Please Try Again")
    elif command == "signup":
        username = input("Create a username: ")
        password = input("create a password: ")
        count = user_list.count_documents({})
        if user_list.find_one({"Username": username}):
            print("That username is taken!")
        else:
            try:
                user_list.insert_one(
                    {"Username": username, "Password": password, "Userid": count}
                )
                userId = count
                loggedIn = True
            except:
                print("An error occured")
    elif command == "quit":
        break
