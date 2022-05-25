import json
import random
import numpy as np
import pandas as pd

with open('./players/input_list.json', 'r') as f: #mat 불러오기
    input_list = json.load(f)
with open('./champion.json', 'r') as f: #mat 불러오기
    champ_list = json.load(f)
input_list_ohe = np.zeros(0)
random.shuffle(input_list)
for i in input_list:
    rand = [0,1,2,3,4]
    random.shuffle(rand)
    a = []
    arr = np.array([np.zeros(159), np.zeros(6),np.zeros(159), np.zeros(6),np.zeros(159), np.zeros(6),np.zeros(159), np.zeros(6),np.zeros(159), np.zeros(6), 0 ])

    for j in rand:
        a.append(i[rand[j]*2])
        a.append(i[rand[j]*2 +1])


    for j in range(5):
        for k in range(len(champ_list)):
            if a[j*2] == int(champ_list[k]["key"]):
                champ = k
                break
        a[j*2] = k
    for j in range(len(a)):
        arr[j][a[j]] = 1
    arr[10] = i[10]
    input_list_ohe = np.append(input_list_ohe, arr, axis=0)
a = np.reshape(input_list_ohe,(-1,11))
a = pd.DataFrame(a, columns=['p1','l1','p2','l2','p3','l3','p4','l4','p5','l5','win'])
print(a.shape)
a.to_json('input_ohe_df.json', orient='table')


# with open('./players/input_list_ohe_np.json', 'w') as f:    #match 저장
#     json.dump(input_list_ohe, f, ensure_ascii=False)



