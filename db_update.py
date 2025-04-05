import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from pymongo import MongoClient
from dotenv import load_dotenv
import os

def geturl():
    load_dotenv()
    sercet = os.getenv("Sercet")
    # Configuration       
    cloudinary.config( 
        cloud_name = "da0ekt7db", 
        api_key = "597192899643245", 
        api_secret = sercet, 
        secure=True
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

            image_url = response['secure_url']

            print(f"Image uploaded successfully. URL: {image_url}")
            return image_url
        except Exception as e:
            print(f"Error uploading image: {e}")
            return None

    blured = []
    unblured = []

    for name in names:
        path = f"NbaPlayer\{name}.jpg"
        url = upload_image(path)
        unblured.append({name:url})

    for name in names:
        path = f"NbaPlayerBlured\{name}-modified.jpg"
        url = upload_image(path)
        blured.append({name:url})

    return unblured,blured