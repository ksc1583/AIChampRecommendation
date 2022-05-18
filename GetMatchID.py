import requests
import json

s = 0
c = 10

api_keys = "RGAPI-8f915ee5-1cad-48e4-bbff-c4932cbd4998"
# request_url = "https://asia.api.riotgames.com/lol/match/v5/matches/"+  +"/ids?type=ranked&start=0&count=20"
def url(puuid, start, count):
    return "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/"+ puuid +"/ids?type=ranked&start="+ f'{start}' +"&count=" + f'{count}'

with open('./players/puuid.json', 'r') as f: #puuid 불러오기
    puuid_data = json.load(f)

print(url(puuid_data[0]["puuid"],s, c))
response = requests.get(url(puuid_data[0]["puuid"],s, c), headers={'X-Riot-Token': api_keys})
print(response.json())