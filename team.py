import requests

url = "https://api.sportradar.com/nba/trial/v7/en/teams/583eca2f-fb46-11e1-82cb-f4ce4684ea4c/profile.json?api_key=uujz5UCqJ2Y8hrU5VnpF6mC23cROB2bFFKBSz4Qa"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
