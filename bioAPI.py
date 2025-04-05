# https://developer.sportradar.com/basketball/v7/reference/nba-player-profile

import requests
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

api_key = os.getenv("BIO_API")

url = f"https://api.sportradar.com/nba/trial/v7/en/players.json?api_key={api_key}"

response = requests.get(url)

if response.status_code == 200:
    players = response.json().get("players", [])

    print(f"Found {len(players)} players.\n")

    # Show the first few players with ID and name
    for player in players[:10]:
        print(f"Name: {player['full_name']}")
        print(f"ID: {player['id']}")
        print("---")
else:
    print(f"Error {response.status_code}: {response.text}")

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

