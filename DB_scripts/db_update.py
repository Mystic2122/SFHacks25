import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from pymongo import MongoClient
from dotenv import load_dotenv
import os


def geturl():
    load_dotenv()
    sercet = os.getenv("CloudSercet")
    # Configuration
    cloudinary.config(
        cloud_name="da0ekt7db",
        api_key="597192899643245",
        api_secret=sercet,
        secure=True,
    )

    load_dotenv()

    username = os.getenv("MONGODB_USERNAME")
    password = os.getenv("MONGODB_PASSWORD")

    s = f"mongodb+srv://{username}:{password}@sfhacks25.ahebnig.mongodb.net/"

    client = MongoClient(s)

    names = [
        "LeBron James",
        "Stephen Curry",
        "Kevin Durant",
        "Giannis Antetokounmpo",
        "Nikola Jokic",
        "Luka Doncic",
        "Jayson Tatum",
        "Anthony Edwards",
        "Ja Morant",
        "Zion Williamson",
        "Devin Booker",
        "Joel Embiid",
        "Damian Lillard",
        "Trae Young",
        "Chris Paul",
        "Bradley Beal",
        "Jamal Murray",
        "Kyrie Irving",
        "Jrue Holiday",
        "Kristaps Porzingis",
        "Rudy Gobert",
        "Karl-Anthony Towns",
        "Brandon Ingram",
    ]

    def upload_image(image_path):
        try:
            # Upload image to Cloudinary
            response = cloudinary.uploader.upload(image_path)

            image_url = response["secure_url"]

            print(f"Image uploaded successfully. URL: {image_url}")
            return image_url
        except Exception as e:
            print(f"Error uploading image: {e}")
            return None

    blured = {}
    unblured = {}

    for name in names:
        path = f"NbaPlayer\{name}.jpg"
        url = upload_image(path)
        unblured[name] = url

    for name in names:
        path = f"NbaPlayerBlured\{name}-modified.jpg"
        url = upload_image(path)
        blured[name] = url

    return unblured, blured

unblured_url, blur_url = geturl()
print(unblured_url)
print('\n\n\n')
print(blur_url)

<<<<<<< HEAD:db_update.py
# username = os.getenv("MONGODB_USERNAME")
# password = os.getenv("MONGODB_PASSWORD")

# s = f"mongodb+srv://{username}:{password}@sfhacks25.ahebnig.mongodb.net/"

# client = MongoClient(s)
# db = client.sports
# players = db.players

# unblured_dict, blured_dict = geturl()
# for name, url in unblured_dict.items():
#     result = players.update_one(
#         {"name": name},  # Match based on the name
#         {"$set": {"unblured_img": url}},  # Update the URL field
#     )
#     if result.modified_count > 0:
#         print(f"Successfully updated {name}'s URL.")
#     else:
#         print(f"No document found for {name} or URL already up-to-date.")

# for name, url in blured_dict.items():
#     result = players.update_one(
#         {"name": name},  # Match based on the name
#         {"$set": {"blured_img": url}},  # Update the URL field
#     )
#     if result.modified_count > 0:
#         print(f"Successfully updated {name}'s URL.")
#     else:
#         print(f"No document found for {name} or URL already up-to-date.")
=======
def uploadURLS():
    load_dotenv()

    username = os.getenv("MONGODB_USERNAME")
    password = os.getenv("MONGODB_PASSWORD")

    s = f"mongodb+srv://{username}:{password}@sfhacks25.ahebnig.mongodb.net/"

    client = MongoClient(s)

    db = client.sports  # Ensure this matches your actual database name
    players = db.players

    unblured_dict, blured_dict = geturl()
    for name, url in unblured_dict.items():
        result = players.update_one(
            {"name": name},  # Match based on the name
            {"$set": {"unblured_img": url}},  # Update the URL field
        )
        if result.modified_count > 0:
            print(f"Successfully updated {name}'s URL.")
        else:
            print(f"No document found for {name} or URL already up-to-date.")

    for name, url in blured_dict.items():
        result = players.update_one(
            {"name": name},  # Match based on the name
            {"$set": {"blured_img": url}},  # Update the URL field
        )
        if result.modified_count > 0:
            print(f"Successfully updated {name}'s URL.")
        else:
            print(f"No document found for {name} or URL already up-to-date.")
>>>>>>> bd7eccafc08d9f59df16693d34eaef6a4fb2fae3:DB_scripts/db_update.py