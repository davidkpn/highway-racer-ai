# balance_data.py
import numpy as np
import pandas as pd
from collections import Counter
from numpy.random import shuffle

train_data = np.load('training_data.npy', allow_pickle=True)

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))
hot_keys = {
            'lefts':[],
            'f_lefts':[],
            'rights':[],
            'f_rights':[],
            'forwards':[],
            'breaks':[]
            }

shuffle(train_data)
# choice = [W,A,S,D]
# count the choices
for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [0,1,0,0]:
        hot_keys['lefts'].append([img,choice])
    elif choice == [1,1,0,0]:
        hot_keys['f_lefts'].append([img,choice])
    elif choice == [1,0,0,0]:
        hot_keys['forwards'].append([img,choice])
    elif choice == [0,0,0,1]:
        hot_keys['rights'].append([img,choice])
    elif choice == [1,0,0,1]:
        hot_keys['f_rights'].append([img,choice])
    elif choice == [0,0,1,0]:
        hot_keys['breaks'].append([img,choice])
    else:
        print('no matches')

min_len = float('inf')
final_data = []
print("before balance action - ")
for key, values in hot_keys.items():
    print(f"number of {key}: {len(values)}")
    if min_len > len(values):
        min_len = len(values)

# The button that has been documented the fewest times is the basis
# for the amount of the other buttons documentation at a ratio of 120%
min_len = int(min_len * 1.2)
for key in hot_keys.keys():
    hot_keys[key] = hot_keys[key][:min_len]
    final_data += hot_keys[key]

print("#"*100)
print("balanced data")
print("#"*100)
for key, values in hot_keys.items():
    print(f"number of {key}: {len(values)}")

shuffle(final_data)
np.save('training_data.npy', final_data)
