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
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical


Championset=pd.read_json('./players/input_list_ohe.json')
inputlist=[0]*5
print(inputlist)
position=input("원하는 포지션을 입력하세요 : ")
if position=="탑":
    a=input("미드 정글 서폿 원딜순으로 챔피언을 입려하세요 : ").split()
    enconded=tokenizer.te
elif position=="미드":
    champion1,champion3,champion4,champion5=input("탑 정글 서폿 원딜순으로 챔피언을 입려하세요 : ").split()
    print( champion1, champion3, champion4, champion5) 
elif position=="정글":
    champion1,champion2,champion4,champion5=input("탑 미드 서폿 원딜순으로 챔피언을 입려하세요 : ").split()
    print( champion1, champion2, champion4, champion5)
elif position=="서폿":
    champion1,champion2,champion3,champion5=input("탑 미드 정글 원딜순으로 챔피언을 입려하세요 : ").split()
    print( champion1, champion2, champion3, champion5) 
elif position=="원딜":
    champion1,champion2,champion3,champion4=input("탑 미드 정글 서폿순으로 챔피언을 입려하세요 : ").split()
    print( champion1, champion2, champion3, champion4)   
else:
    print("잘못입력하셨습니다.")
    