import requests
import json

url = "http://ddragon.leagueoflegends.com/cdn/12.9.1/data/en_US/champion.json"
name = []
response = requests.get(url)
champion = []
# with open('./players/champion.json', 'r') as f: #puuid 불러오기
#     puuid_data = json.load(f)

print(len(response.json()['data']))
for i in response.json()['data']:
    name.append(i)
# print(name)

for i in range(len(response.json()['data'])):
    champion.append({"key": response.json()['data'][name[i]]["key"], "name": name[i],
                               "tags": response.json()['data'][name[i]]["tags"]})

with open('./champion.json', 'w') as f:  # puuid 저장
    json.dump(champion, f, ensure_ascii=False, indent=4)
