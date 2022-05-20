import requests
import json
import time

api_keys =["RGAPI-8f915ee5-1cad-48e4-bbff-c4932cbd4998",
           "RGAPI-9a34ab21-00ec-4a0b-9975-dda1e689be61",
           "RGAPI-8bbcc5ea-199c-4026-9668-3abd63bc2f67",
           "RGAPI-29d97310-c897-4212-9c2f-e3ebac8e3e74",
           "RGAPI-233d7d9c-6234-4c92-b331-80ae3a153510",
           "RGAPI-f955eae2-6f0e-40ea-a2e8-2a73b87f6b02"]
url = 'https://asia.api.riotgames.com/lol/match/v5/matches/'

with open('./players/match_list.json', 'r') as f: #puuid 불러오기
    match_data = json.load(f)

with open('./players/input_list.json', 'r') as f: #puuid 불러오기
    input_list = json.load(f)

i = 10368

def collect_data(respon):
    respon_json = respon.json()
    win_list = []
    lost_list = []
    for i in respon_json["info"]["participants"]:
        if i["win"]:
            win_list.append(int(i["championId"]))
            if i["teamPosition"] == "TOP":
                win_list.append(0)
            elif i["teamPosition"] == "JUNGLE":
                win_list.append(1)
            elif i["teamPosition"] == "MIDDLE":
                win_list.append(2)
            elif i["teamPosition"] == "BOTTOM":
                win_list.append(3)
            elif i["teamPosition"] == "UTILITY":
                win_list.append(4)
            else:
                win_list.append(5)
        else:
            lost_list.append(int(i["championId"]))
            if i["teamPosition"] == "TOP":
                lost_list.append(0)
            elif i["teamPosition"] == "JUNGLE":
                lost_list.append(1)
            elif i["teamPosition"] == "MIDDLE":
                lost_list.append(2)
            elif i["teamPosition"] == "BOTTOM":
                lost_list.append(3)
            elif i["teamPosition"] == "UTILITY":
                lost_list.append(4)
            else:
                lost_list.append(5)
    win_list.append(1)
    lost_list.append(0)
    return win_list, lost_list
            

while i < len(match_data):

    response0 = requests.get(url + match_data[i], headers={'X-Riot-Token': api_keys[0]})
    response1 = requests.get(url + match_data[i+1], headers={'X-Riot-Token': api_keys[1]})
    response2 = requests.get(url + match_data[i+2], headers={'X-Riot-Token': api_keys[2]})
    response3 = requests.get(url + match_data[i+3], headers={'X-Riot-Token': api_keys[3]})
    response4 = requests.get(url + match_data[i+4], headers={'X-Riot-Token': api_keys[4]})
    response5 = requests.get(url + match_data[i+5], headers={'X-Riot-Token': api_keys[5]})
    if (response0.status_code==200 and response1.status_code==200 and response2.status_code==200
            and response3.status_code==200 and response4.status_code==200 and response5.status_code==200):
        w, l = collect_data(response0)
        input_list.append(w)
        input_list.append(l)
        w, l = collect_data(response1)
        input_list.append(w)
        input_list.append(l)
        w, l = collect_data(response2)
        input_list.append(w)
        input_list.append(l)
        w, l = collect_data(response3)
        input_list.append(w)
        input_list.append(l)
        w, l = collect_data(response4)
        input_list.append(w)
        input_list.append(l)
        w, l = collect_data(response5)
        input_list.append(w)
        input_list.append(l)

        with open('./players/input_list.json', 'w') as f:    #match 저장
            json.dump(input_list, f, ensure_ascii=False, indent=4)
        print(i)
        i+=6
    else:
        print(response0.status_code)
        time.sleep(120)
        