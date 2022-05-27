#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import random
import numpy as np
import pandas as pd

with open('./players/input_list.json', 'r') as f: #mat 불러오기
    input_list = json.load(f)
with open('champion.json', 'r') as f: #mat 불러오기
    champ_list = json.load(f)

bottomDuoList=np.array([])
winList=np.array([])
for i in input_list:
    for j in range(len(i)):
        l=np.array([])
        if j%2==1:
            if i[j]==3:
                a=np.append(l,i[j-1])
            elif i[j]==4:
                b=np.append(l,i[j-1])
            else:
                pass
    k = np.concatenate((a, b), axis=0)
    bottomDuoList=np.append(bottomDuoList,k)
    winList=np.append(winList,i[-1])


print(bottomDuoList.reshape(-1,2).shape)
bottomDuoList=np.reshape(bottomDuoList,(-1,2))


winList=np.reshape(winList,(-1,1))

winList.shape


# In[7]:


finalList = np.concatenate((bottomDuoList, winList), axis=1)


# In[8]:


finalList


# model

# In[9]:


from abc import ABC, abstractmethod
from sklearn.model_selection import train_test_split
import keras


# In[10]:


class BaseModel(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def build(self):
        pass
    
class DenseDegressive(BaseModel):
    def __init__(self, Xlist, ylist,n_hidden_layers, NN, dropout, batch_size=1000, epochs=10):
        self.Xlist=Xlist
        self.ylist=ylist
        self.n_hidden_layers = n_hidden_layers
        self.NN = NN
        self.dropout = dropout
        self.batch_size = batch_size  # The higher the better, but need more gpu memory
        self.epochs = epochs  # In order to not be overflowed by training/testing logs

    def build(self):

        self.model = keras.models.Sequential()
        self.model.add(keras.layers.Dense(units=self.NN, input_shape=(159,), activation='relu'))
        self.model.add(keras.layers.Dropout(self.dropout))
        for k in range(self.n_hidden_layers):  # hidden layers
            units = self.NN // (2**(k+1))
            self.model.add(keras.layers.Dense(units=units, activation='relu'))
            self.model.add(keras.layers.Dropout(self.dropout))
        self.model.add(keras.layers.Dense(units=1, activation='sigmoid'))  # reading output
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[11]:


def q():
    input_list = finalList
    with open('champion.json', 'r') as f: #mat 불러오기
        champ_list = json.load(f)
    input_list_ohe = np.zeros(0)
    random.shuffle(input_list)
    for i in input_list:
        print(i)
        rand = [0,1]
        random.shuffle(rand)
        a = []
        arr = np.array(np.zeros(160))

        for j in rand:
            a.append(i[rand[j]])


        for j in range(2):
            for k in range(len(champ_list)):
                if a[j] == int(champ_list[k]["key"]):
                    arr[k]=1
                    break
        arr[159] = i[2]
        input_list_ohe = np.append(input_list_ohe, arr, axis=0)
    a = np.reshape(input_list_ohe,(-1,160))
    print(a.shape)
    return a


# In[12]:


dataset=q()
X=dataset[:,0:159]
y=dataset[:,159]



X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.3, random_state=1)
n = DenseDegressive(Xlist=X_train, ylist=y_train, n_hidden_layers=5, NN=1024, dropout=0.2, batch_size=1000, epochs=200)
result=n.build()
print(result)
n.model.summary()


history=n.model.fit(X_train, y_train, batch_size=1000, epochs=200)


# In[15]:


# predict 10 random game data
y_predicted = n.model.predict(X_test)

for _ in range(0, 50):
    random_index = random.randint(0, X_test.shape[0]-1)
    print("index: ", random_index,
          "actual y: ", y_test[random_index],
          "predicted y: ", y_predicted[random_index])

# evaluate test set
evaluation = n.model.evaluate(X_test, y_test)

print('loss: ', evaluation[0])
print('accuracy', evaluation[1])


# 훈련 정확도

# In[16]:


history_dict=history.history
history_dict.keys()


# In[17]:


import matplotlib.pyplot as plt
plt.clf() # 그래프를 초기화합니다.
acc = history_dict['accuracy']
loss = history_dict['loss']
#val_acc = history_dict['val_acc']
epochs = range(1, len(loss) + 1)
plt.plot(epochs, acc, 'bo', label='Training acc')
#plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training  accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()


# 모델 저장
# 

# In[18]:


# 6. 모델 저장하기
from keras.models import load_model
n.model.save('bottom_duo_model.h5')


# 모델 불러오기

# In[28]:



# 0. 사용할 패키지 불러오기


'''

# 1. 실무에 사용할 데이터 준비하기
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_test = x_test.reshape(10000, 784).astype('float32') / 255.0
y_test = np_utils.to_categorical(y_test)
xhat_idx = np.random.choice(x_test.shape[0], 5)
xhat = x_test[xhat_idx] 
'''


# 2. 모델 불러오기
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from numpy import argmax
from keras.models import load_model
model = load_model('bottom_duo_model.h5')

# 3. 모델 사용하기
yhat = model.predict(X_test)


for _ in range(0, 50):
    random_index = random.randint(0, X_test.shape[0]-1)
    print("index: ", random_index,
          "actual y: ", y_test[random_index], #고쳐야할듯
          "predicted y: ", yhat[random_index])

    


# In[ ]:




