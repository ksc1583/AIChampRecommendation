import json
import random

with open('./players/input_list.json', 'r') as f: #mat 불러오기
    input_list = json.load(f)
with open('./champion.json', 'r') as f: #mat 불러오기
    champ_list = json.load(f)

input_list_ohe = []
random.shuffle(input_list)
for i in input_list:
    rand = [0,1,2,3,4]
    random.shuffle(rand)
    print(i)
    shuffle_list = []

    for j in rand:
        shuffle_list.append(i[rand[j]*2])
        shuffle_list.append(i[rand[j]*2 + 1])


    for j in range(5):
        champ = [0 for t in range(159)]
        for k in range(len(champ_list)):
            if shuffle_list[j*2] == int(champ_list[k]["key"]):
                champ[k] = 1
                break
        shuffle_list[j*2] = champ

    for j in range(5):
        lane = [0 for t in range(6)]
        lane[shuffle_list[j*2 + 1]] = 1
        shuffle_list[j*2 + 1] = lane

    shuffle_list.append(i[-1])
    input_list_ohe.append(shuffle_list)
with open('./players/input_list_ohe.json', 'w') as f:    #match 저장
    json.dump(input_list_ohe, f, ensure_ascii=False)



