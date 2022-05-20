import requests
import json


with open('./players/match.json', 'r') as f: #puuid 불러오기
    match = json.load(f)

print(len(match))
match_list = list(set(match))
print(len(match_list))

with open('./players/match_list.json', 'w') as f:    #puuid 저장
    json.dump(match_list, f, ensure_ascii=False, indent=4)


    #for i in range(len(response.json())):
    #get_puuid(response.json()[i]['summonerName'])
    #print(response.json()[i]['summonerName'])

