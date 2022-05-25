from scipy import rand
import tensorflow
import os
import json
import random
import keras
import sklearn
from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation



os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

class BaseModel(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def build(self):
        pass




# Training/Testing accuracy:
# games=145358, options=(BR_Mode, 1, 256, 0.3): 0.5458/0.5321
# games=145358, options=(BR_Mode, 2, 128, 0.2): 0.5427/0.5330
# games=145358, options=(BR_Mode, 2, 256, 0.3): 0.5420/0.5332
# games=145358, options=(BR_Mode, 2, 512, 0.5): 0.5405/0.5312


# Training/Testing accuracy:
# games=145358, options=(BR_Mode, 3, 256, 0.3): 0.5371/0.5327
# games=145358, options=(BR_Mode, 3, 512, 0.3): 0.5319/0.5317
# games=148883 , options=(ABOTJMCS_Mode, 4, 512, 0.0): 0.5302/0.5272
# games=148883, options=(ABOTJMCS_Mode, 3, 512, 0.2): 0.5274/0.5297
# games=148883, options=(ABOTJMCS_Mode, 3, 1024, 0.3): 0.5274/0.5257
# games=148883, options=(ABOTJMCS_Mode, 3, 1024, 0.1): 0.5313/0.5262
class DenseDegressive(BaseModel):
    def __init__(self, Xlist, ylist,n_hidden_layers, NN, dropout, batch_size=1000, epochs=10):
        self.Xlist=Xlist
        self.ylist=ylist
        self.n_hidden_layers = n_hidden_layers
        self.NN = NN
        self.dropout = dropout
        self.model = None
        self.batch_size = batch_size  # The higher the better, but need more gpu memory
        self.epochs = epochs  # In order to not be overflowed by training/testing logs

    def build(self):

        self.model = keras.models.Sequential()
        self.model.add(keras.layers.Dense(units=self.NN, input_shape=(10,), activation='relu'))
        self.model.add(keras.layers.Dropout(self.dropout))
        for k in range(self.n_hidden_layers):  # hidden layers
            units = self.NN // (2**(k+1))
            self.model.add(keras.layers.Dense(units=units, activation='relu'))
            self.model.add(keras.layers.Dropout(self.dropout))
        self.model.add(keras.layers.Dense(units=1, activation='sigmoid'))  # reading output
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        # return self.model

#importing Categorical data

dataset1=pd.read_json('./players/input_list_ohe.json')
#print(dataset1)
X=dataset1.iloc[:,0:10].values
y=dataset1.iloc[:,10].values

#X=dataset.drop(10,axis=1).values
#y=dataset[10].values
#X=dataset.iloc[:,0:10].values
#y=dataset.iloc[:,10].values


#print(X)
#print(y)
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.3, random_state=1)


#print("hi")
#X=dataset.iloc[:,:].values
#y=dataset.iloc[:,10].values

#spitting the dataset into the Training set and Test set
#X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.3, random_state=1)

#train test validation 사용할때
#X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.5, random_state=1)
#X_val, X_test, y_val, y_test=train_test_split(X, y, test_size=0.4, random_state=1)

#Feature scaling 정규화
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
#X_val=sc.transform(X_val)



n = DenseDegressive(Xlist=X_train, ylist=y_train, n_hidden_layers=5, NN=1024, dropout=0.2, batch_size=1000, epochs=10)
result=n.build()
print(result)
n.model.summary()


history = n.model.fit(X_train, y_train, batch_size=1000, epochs=10)


#train test validation 사용할때 수정필요
#history = n.model.fit(X_train, y_train, epochs=4, batch_size=1000, validation_data=(X_val, y_val))

# predict 10 random game data
y_predicted = n.model.predict(X_test)

for X in range(0, 20):
    random_index = random.randint(0, X_test.shape[0]-1)
    print("index: ", random_index,
          "actual y: ", y_test[random_index],
          "predicted y: ", y_predicted[random_index])

# evaluate test set
evaluation = n.model.evaluate(X_test, y_test)

print('loss: ', evaluation[0])
print('accuracy', evaluation[1])

#출력값

#position=input("원하는 포지션을 입력하세요 : ")
#if position=="탑":
#    champion2,champion3,champion4,champion5=input("미들 정글 서폿 원딜순으로 챔피언을 입려하세요")
#print("hi")
