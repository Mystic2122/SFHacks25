import requests
import os
from dotenv import load_dotenv
import time


player_ids = [
    "bf9ad0fd-0cb8-4360-8970-5f1b5cf3fa8d",
    "5382cf43-3a79-4a5a-a7fd-153906fe65dd",
    "6c60282d-165a-4cba-8e5a-4f2d9d4c5905",
    "65700e81-3aa0-49a9-8a94-004f2cfb64e5",
    "98136da3-452f-49dc-a794-1ee9c76443f2",
    "3e492a6a-ed3c-499d-b3f5-ff68ca16f6fd",
    "9983bed6-e53c-4c65-a90a-51546a0e3352",
    "cf418e0c-de9d-438f-a1ac-3be539a56c42",
    "ab532a66-9314-4d57-ade7-bb54a70c65ad",
    "0afbe608-940a-4d5d-a1f7-468718c67d91",
    "dd146010-902b-4ad7-b98c-650d0363a2f0",
    "685576ef-ea6c-4ccf-affd-18916baf4e60",
    "5cc51c05-06f5-4ae4-89a4-1d329fbbcdfb",
    "8082841d-e516-43c6-a81b-7987fa321acd",
    "942c53e3-7268-44e3-b0a9-fdff55a72c03",
    "31baa84f-c759-4f92-8e1f-a92305ade3d6",
    "53f2fa48-e61b-49fb-843d-8a3e872257eb",
    "ff461754-ad20-4eeb-af02-2b46cc980b24",
    "37fbc3a5-0d10-4e22-803b-baa2ea0cdb12",
    "d0c7135a-1aea-40cb-ba20-df656de71749",
    "8ec91366-faea-4196-bbfd-b8fab7434795",
]


def height_conversion(h):
    feet = h // 12
    inches = h % 12
    return str(feet) + "' " + str(inches) + '"'


# def get_teams()
load_dotenv()
api_key = os.getenv("BIO_API")

player_data = []

for player_id in player_ids:
    url = f"https://api.sportradar.com/nba/trial/v7/en/players/{player_id}/profile.json?api_key={api_key}"
    headers = {"accept": "application/json"}

    # Send the GET request
    response = requests.get(url, headers=headers)

    # Parse the response as JSON
    if response.status_code == 200:
        cur_data = response.json()
        name = cur_data["full_name"]
        height = height_conversion(cur_data["height"])
        position = cur_data["primary_position"]
        jersey = cur_data["jersey_number"]
        if "college" in list(cur_data.keys()):
            college = cur_data["college"]
        else:
            collge = None

        url = f"http://rest.nbaapi.com/api/PlayerDataAdvanced/name/{name}"

        response = requests.get(url)
        data = response.json()
        sorted_data = sorted(data, key=lambda x: x["age"])

        teams = []
        positions = []
        for season in sorted_data:
            positions.append(season["position"])
            teams.append(season["team"])

        player_data.append(
            {
                "name": name,
                "age": data[-1]["age"],
                "height": height,
                "position": position,
                "teams": set(teams),
                "jersey": jersey,
                "college": college,
            }
        )

    else:
        print(
            f"Failed to retrieve data for player {player_id}. Status code: {response.status_code}"
        )

    # Sleep for 0.5 seconds before making the next request to avoid rate limit issues
    time.sleep(0.5)
"""
fields of interest:
full_name
height
primary_position
jersey_number
college
teams are from other API
"""

print(player_data)
