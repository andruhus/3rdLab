from OneStream import OneStream
from MultiStream import MultiStream
if __name__ == '__main__':
    one = OneStream()
    one.print_results()
    one.get_partial_accuracy()

    mul = MultiStream()
    mul.print_results()
    mul.get_partial_accuracy()

# import pandas as pd
#
# train = pd.read_csv('data/train.csv',index_col='PassengerId')
# test = pd.read_csv('data/test.csv',index_col='PassengerId')
# bad_keys = ['Age','Cabin','Embarked','Fare']
# nan_val = [train[train['Age'].notnull()]['Age'].mean(),'NO','N',train[train['Fare'].notnull()]['Fare'].mean()]
# nan_val_test = [test[test['Age'].notnull()]['Age'].mean(),'NO','N',test[test['Fare'].notnull()]['Fare'].mean()]
# for index in range(len(bad_keys)):
#     a = bad_keys[index]
#     train.loc[train[a].isna(),a] = nan_val[index]
#     test.loc[test[a].isna(),a] = nan_val_test[index]
#
# # # train.to_csv('data/train.csv')
# # # test.to_csv('data/test.csv')
# for key in test.keys():
#     if len(train[train[key].isna()]) > 0:
#         print(train[train[key].isna()])
#     if len(test[test[key].isna()]) > 0:
#         print(test[test[key].isna()])
#
# #
# # test.loc[test['Fare'].isnull(),'Fare'] = test['Fare'].mean()
# # print(train['Age'].mean())
# # train.loc[train['Age'] == -1.0] = train[train['Age'] != -1.0]['Age'].mean()
# # print(train['Age'].mean())
# #
# # print(test['Age'].mean())
# # test.loc[test['Age'] == -1.0] = test[test['Age'] != -1.0]['Age'].mean()
# # print(test['Age'].mean())
# # print(test.loc[test['Fare'].isnull(),'Fare'])
# #
# # train.to_csv('data/train.csv')
# test.to_csv('data/test.csv')
