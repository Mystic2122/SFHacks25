import requests
import time
import os
from dotenv import load_dotenv


# Retry function with exponential backoff for API requests
def get_data_with_retry(url, headers, max_retries=5, backoff_factor=2):
    retries = 0
    while retries < max_retries:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()  # Successfully retrieved data
        elif response.status_code == 429:  # Rate limit exceeded
            retries += 1
            wait_time = backoff_factor**retries  # Exponential backoff
            print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)  # Wait before retrying
        else:
            # Handle other status codes (e.g., 500, 400, etc.)
            print(f"Request failed with status code {response.status_code}.")
            break

    print("Max retries reached. Could not retrieve data.")
    return None


load_dotenv()
api_key = os.getenv("BIO_API")
url = f"https://api.sportradar.com/nba/trial/v7/en/league/teams.json?api_key={api_key}"
headers = {"accept": "application/json"}

teams_data = get_data_with_retry(url, headers)


nba_teams = [
    "Hawks",
    "Celtics",
    "Nets",
    "Hornets",
    "Bulls",
    "Cavaliers",
    "Mavericks",
    "Nuggets",
    "Pistons",
    "Warriors",
    "Rockets",
    "Pacers",
    "Clippers",
    "Lakers",
    "Grizzlies",
    "Heat",
    "Bucks",
    "Timberwolves",
    "Pelicans",
    "Knicks",
    "Thunder",
    "Magic",
    "76ers",
    "Suns",
    "Trail Blazers",
    "Kings",
    "Spurs",
    "Raptors",
    "Jazz",
    "Wizards",
]

team_ids = []
for team in teams_data.get("teams", []):
    if team["name"] in nba_teams:
        team_ids.append(team["id"])
        print(f"Found team: {team['name']}")


nba_players = [
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
player_ids = []

for team_id in team_ids:

    team_url = f"https://api.sportradar.com/nba/trial/v7/en/teams/{team_id}/profile.json?api_key={api_key}"
    roster_data = get_data_with_retry(team_url, headers)

    if not roster_data:
        continue

    for player in roster_data.get("players", []):
        full_name = player["full_name"]
        if full_name in nba_players:
            print(player)
            print(
                f"ID: {player['id']}\nName: {player['full_name']}\nHeight: {player['height']}\n"
                f"Position: {player['primary_position']}\nJersey Number: {player['jersey_number']}"
            )
            player_ids.append(player["id"])

        time.sleep(0.01)

print(player_ids)
