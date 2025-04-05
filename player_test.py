import requests

url = "https://api.sportradar.com/nba/trial/v7/en/players/8ec91366-faea-4196-bbfd-b8fab7434795/profile.json?api_key=uujz5UCqJ2Y8hrU5VnpF6mC23cROB2bFFKBSz4Qa"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
