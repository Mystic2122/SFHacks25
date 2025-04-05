import requests

first_last_name = "Lebron James"

url = f"http://rest.nbaapi.com/api/PlayerDataAdvanced/name/{first_last_name}"


response = requests.get(url)
data = response.json()
print(data[-1])
sorted_data = sorted(data, key=lambda x: x["age"])

teams = []
positions = []
for season in sorted_data:
    positions.append(season["position"])
    teams.append(season["team"])


print(set(teams))
print(data[-1]["age"])
