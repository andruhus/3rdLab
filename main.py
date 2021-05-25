# from OneStream import OneStream
# from MultiStream import MultiStream
#
# one = OneStream()
# one.print_results()
# one.get_partial_accuracy()
#
# mul = MultiStream()
# mul.print_results()
# mul.get_partial_accuracy()

import pandas as pd

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')
bad_keys = ['Age','Cabin','Embarked']
nan_val = [-1.0,'NO','N']
for index in range(len(bad_keys)):
    a = bad_keys[index]
    train.loc[train[a].isna(),a] = nan_val[index]
    test.loc[test[a].isna(),a] = nan_val[index]

print(train[train[bad_keys].isna()])
print(test[test[bad_keys].isna()])
print(train.head())
print(test.head())