import requests
import json

api_keys = "RGAPI-8f915ee5-1cad-48e4-bbff-c4932cbd4998"
request_url_TopPlayers = "https://kr.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/MASTER/I?page=1"
request_url_puuid = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/'

response = requests.get(request_url_TopPlayers, headers={'X-Riot-Token': api_keys})

def get_puuid(player_name):   #get player puuid for
    response_data = requests.get(request_url_puuid + player_name, headers={'X-Riot-Token': api_keys})
    print(response_data.json())

print("status_code: {}".format(response.status_code))
if response.status_code == 200:
    player_list = response.json()
    print(player_list)
    with open('./MASTER_data.json', 'w') as f:
        json.dump(player_list, f, ensure_ascii=False, indent=4)

    #for i in range(len(response.json())):
    #get_puuid(response.json()[i]['summonerName'])
    #print(response.json()[i]['summonerName'])

