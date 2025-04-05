# https://developer.sportradar.com/basketball/v7/reference/nba-player-profile

import requests
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

api_key = os.getenv("BIO_API")

url = f"https://api.sportradar.com/nba/trial/v7/en/players/8ec91366-faea-4196-bbfd-b8fab7434795/profile.json?api_key={api_key}"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)
print(response.text)
