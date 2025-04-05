import requests

url = "https://api.sportradar.com/nba/trial/v7/en/league/teams.json?api_key=uujz5UCqJ2Y8hrU5VnpF6mC23cROB2bFFKBSz4Qa"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
