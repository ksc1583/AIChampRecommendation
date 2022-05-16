import json
import requests

api_keys = ""
request_url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/"

tier = ['CHALLENGER','GRANDMASTER','MASTER']
tier_in = tier[2]
page = 14

with open('./players/puuid.json', 'r') as f: #puuid 불러오기
    puuid_data = json.load(f)

for j in range(12, page):
    with open('./players/' + tier_in + '_data' + f'{j+1}' + '.json', 'r') as f: #player 정보 불러오기
        json_data = json.load(f)

    #print(json.dumps(json_data,  indent="\t", ensure_ascii = False) )
    i = 0
    while i < len(json_data):
        print('page: ',j+1, i)
        response = requests.get(request_url + json_data[i]['summonerId'], headers={'X-Riot-Token': api_keys})
        print(json_data[i]['summonerName'])
        if response.status_code == 200:
            puuid_data.append({"summonerName": json_data[i]['summonerName'], "summonerId": json_data[i]['summonerId'],
                               "puuid": response.json()['puuid']})
            i+=1
        else:
            print(response.status_code)
    with open('./players/puuid.json', 'w') as f:  # puuid 저장
        json.dump(puuid_data, f, ensure_ascii=False, indent=4)

# for i in range(len(json_data)):
#     print(i)
#     response = requests.get(request_url + json_data[i]['summonerId'], headers={'X-Riot-Token': api_keys})
#     print(json_data[i]['summonerName'])
#     if response.status_code == 200:
#         puuid_list.append({"summonerName" : json_data[i]['summonerName'], "summonerId" : json_data[i]['summonerId'], "puuid" : response.json()['puuid']})
#     else:
#         print(response.status_code)
#         i = i -1

with open('./players/puuid.json', 'w') as f:    #puuid 저장
    json.dump(puuid_data, f, ensure_ascii=False, indent=4)
