import requests

url = "https://api.sportradar.com/nba/trial/v7/en/league/teams.json?api_key=uujz5UCqJ2Y8hrU5VnpF6mC23cROB2bFFKBSz4Qa"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

teams_data = response.json()
team_id = []
for team in teams_data["teams"]:
    team_id.append(team["id"])

print(team_id)

player_id = []
for team in team_id:
    url = "https://api.sportradar.com/nba/trial/v7/en/teams/{team_id}/profile.json?api_key=uujz5UCqJ2Y8hrU5VnpF6mC23cROB2bFFKBSz4Qa"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    roster_data = response.json()
    for player in roster_data["players"]:
        player_id.append(player["id"])
