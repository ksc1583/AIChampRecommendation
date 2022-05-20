import requests
import json
import time

s = 1
c = 10
with open('./players/match.json', 'r') as f: #mat 불러오기
    match = json.load(f)
api_keys = "RGAPI-8f915ee5-1cad-48e4-bbff-c4932cbd4998"
# request_url = "https://asia.api.riotgames.com/lol/match/v5/matches/"+  +"/ids?type=ranked&start=0&count=20"
def url(puuid, start, count):
    return "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/"+ puuid +"/ids?type=ranked&start="+ f'{start}' +"&count=" + f'{count}'

with open('./players/puuid.json', 'r') as f: #puuid 불러오기
    puuid_data = json.load(f)

i = 1
while i < len(puuid_data):
    response = requests.get(url(puuid_data[i]["puuid"],s, c), headers={'X-Riot-Token': api_keys})
    if response.status_code == 200:
        for j in response.json():
            match.append(j)
        with open('./players/match.json', 'w') as f:  # match 저장
            json.dump(match, f, ensure_ascii=False, indent=4)
        print(i)
        i+=1
    else:
        print(response.status_code)
        time.sleep(120)



with open('./players/match.json', 'w') as f:    #match 저장
    json.dump(match, f, ensure_ascii=False, indent=4)


