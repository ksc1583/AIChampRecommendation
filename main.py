import requests
import json

api_keys = "RGAPI-8f915ee5-1cad-48e4-bbff-c4932cbd4998"
request_url_puuid = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/'


def get_puuid(player_name):   #get player puuid for
    response_data = requests.get(request_url_puuid + player_name, headers={'X-Riot-Token': api_keys})
    print(response_data.json())


    #for i in range(len(response.json())):
    #get_puuid(response.json()[i]['summonerName'])
    #print(response.json()[i]['summonerName'])

