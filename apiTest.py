import requests

url = "http://rest.nbaapi.com/api/PlayerDataAdvanced/name/Lebron"

response = requests.get(url)

print(response.json()[-1])