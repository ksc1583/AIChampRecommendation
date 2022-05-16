import requests
import json

api_keys = ""

tier = "CHALLENGER"
page = "2"

request_url_TopPlayers = "https://kr.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/"+tier+"/I?page="+page
response = requests.get(request_url_TopPlayers, headers={'X-Riot-Token': api_keys})

print("status_code: {}".format(response.status_code))
if response.status_code == 200:
    player_list = response.json()
    print(len(player_list))
    print(player_list)
    with open('./players/'+ tier +'_data'+page+'.json', 'w') as f:
        json.dump(player_list, f, ensure_ascii=False, indent=4)
