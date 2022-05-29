from scipy import rand
import tensorflow
import os
import json
import random
import keras
import sklearn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import input_onehot



dataset=pd.read_json('./players/input_list.json')
#print(dataset1)_

#dataset=input_onehot.q()
#print(dataset.info())
#dataset = dataset1.astype(float)
X1=dataset.iloc[:,0].values
X2=dataset.iloc[:,2].values
X3=dataset.iloc[:,4].values
X4=dataset.iloc[:,6].values
X5=dataset.iloc[:,8].values
#y=dataset[:,159]
print(X1[0],X2[0])
y=[]
for i in range(len(X1)):
   y.append(X1[i]*X2[i]*X3[i]*X4[i]*X5[i])
print(type(y[0]))
print(len(set(y)))