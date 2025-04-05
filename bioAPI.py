# https://developer.sportradar.com/basketball/v7/reference/nba-player-profile

import requests
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

api_key = os.getenv("BIO_API")
player_id = "8ec91366-faea-4196-bbfd-b8fab7434795"

url = f"https://api.sportradar.com/nba/trial/v7/en/players.json?api_key={api_key}"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)
print(response.json())
data = response.json()
print(data["college"])
print(data["jersey_number"])
print(data["primary_position"])
print(data["experience"])
print(data["birth_place"])
print(data["height"])

height= data["height"]
def height_convertion(height):
    inches= height%12
    feet= height//12
    return f"{feet}'{inches}\""

print(height_convertion(height))

players= [
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
    "Shai Gilgeous-Alexander",
    "Tyrese Haliburton",
    "Donovan Mitchell",
    "De'Aaron Fox",
    "LaMelo Ball",
    "Jimmy Butler",
    "Paul George",
    "Kawhi Leonard",
    "Rudy Gobert",
    "Karl-Anthony Towns",
    "Kyrie Irving",
    "Cade Cunningham",
    "Paolo Banchero",
    "Victor Wembanyama",
    "Chet Holmgren",
    "Evan Mobley",
    "Scottie Barnes",
    "Tyrese Maxey",
    "Anfernee Simons",
    "Bennedict Mathurin",
    "Shaedon Sharpe",
    "Chris Paul",
    "Russell Westbrook",
    "DeMar DeRozan",
    "Jrue Holiday",
    "Pascal Siakam",
    "Brandon Ingram",
    "Jamal Murray",
    "Domantas Sabonis",
    "Bam Adebayo",
    "Jaren Jackson Jr.",
    "Kristaps Porzingis",
    "Darius Garland",
    "Bradley Beal",
    "Dejounte Murray",
    "Mikal Bridges",
    "Herb Jones",
    "Keegan Murray",
    "Walker Kessler",
    "Franz Wagner"
]


