# # https://developer.sportradar.com/basketball/v7/reference/nba-player-profile

# import requests
# import os
# from dotenv import load_dotenv

# # Load the environment variables from the .env file
# load_dotenv()

# api_key = os.getenv("BIO_API")
# player_id = "8ec91366-faea-4196-bbfd-b8fab7434795"

# url = f"https://api.sportradar.com/nba/trial/v7/en/players.json?api_key={api_key}"

# headers = {"accept": "application/json"}

# response = requests.get(url, headers=headers)
# print(response.json())
# # data = response.json()
# # print(data["college"])
# # print(data["jersey_number"])
# # print(data["primary_position"])
# # print(data["experience"])
# # print(data["birth_place"])
# # print(data["height"])

# # height= data["height"]
# # def height_convertion(height):
# #     inches= height%12
# #     feet= height//12
# #     return f"{feet}'{inches}\""

# # print(height_convertion(height))
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("BIO_API")
<<<<<<< HEAD
player_id = "8ec91366-faea-4196-bbfd-b8fab7434795"
# /{player_id}/profile
=======

>>>>>>> 0c6a453d75ea75958f742c569b9b1c2c385d8442
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

<<<<<<< HEAD
response = requests.get(url, headers=headers)
data = response.json()
print(data)
=======
>>>>>>> 0c6a453d75ea75958f742c569b9b1c2c385d8442
