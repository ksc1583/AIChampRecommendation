import json
import random
import numpy as np
import pandas as pd

def q():
    with open('./players/input_list.json', 'r') as f: #mat 불러오기
        input_list = json.load(f)
    with open('./champion.json', 'r') as f: #mat 불러오기
        champ_list = json.load(f)
    input_list_ohe = np.zeros(0)
    random.shuffle(input_list)
    for i in input_list:
        print(i)
        rand = [0,1,2,3,4]
        random.shuffle(rand)
        a = []
        arr = np.array(np.zeros(160))

        for j in rand:
            a.append(i[rand[j]*2])


        for j in range(5):
            for k in range(len(champ_list)):
                if a[j] == int(champ_list[k]["key"]):
                    arr[k]=1
                    break
        arr[159] = i[10]
        input_list_ohe = np.append(input_list_ohe, arr, axis=0)
    a = np.reshape(input_list_ohe,(-1,160))
    print(a.shape)
    return a



# with open('./players/input_list_ohe_np.json', 'w') as f:    #match 저장
#     json.dump(input_list_ohe, f, ensure_ascii=False)



