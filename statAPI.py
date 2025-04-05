import requests

first_last_name = "Lebron James"

url = f"http://rest.nbaapi.com/api/PlayerDataAdvanced/name/{first_last_name}"


response = requests.get(url)
data = response.json()
print(data[0].keys())
# sorted_data = sorted(data, key=lambda x: x["age"])

# for season in sorted_data:
#     print(season["team"])
