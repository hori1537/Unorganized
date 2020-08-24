

import sklearn
import sklearn.tree
import numpy as np
import random
import pandas as pd

from sklearn.ensemble import RandomForestRegressor

x = []
y=[]


for i in range(30):
    b = random.random()
    c = random.random()
    d = random.random()
    
    tmp = -b+c+2*d
    
    x.append([b,c,d])
    y.append(tmp)



x = np.array(x)
x = pd.DataFrame(x)
x.columns  = ['b', 'c', 'd']
features =  ['b', 'c', 'd']

y= np.array(y)
y = pd.DataFrame(y)


print(x)
print(y)

n_estimators = 4
max_depth = 4
model = RandomForestRegressor(n_estimators=n_estimators, max_depth = 4)
model.fit(x,y)

_score = model.score(x,y)
print(_score)

for i_sample in range(len(x)):
    for i_estimator, tree in enumerate(model.estimators_):
        
        path =  tree.decision_path(x)
        #print(path)

        print('i_estimator ', i_estimator)
        new_array = np.array(path.todense())[i_sample]
        print(i_sample)
        #print(dense)
        new_path = []
        for i in range(len(new_array)):
            if new_array[i] == 1:
                new_path.append(i)
        #print(new_path)

        for i in range(1, len(new_path)):
            label = features[tree.tree_.feature[new_path[i-1]]]
            value_ = tree.tree_.value[new_path[i-1]]
            if new_path[i] - new_path[i-1] == 1:
                label = label + " ≦ "
            else:
                label = label + " > "
            print(label + str(tree.tree_.threshold[new_path[i-1]]))
            print(value_)