import pandas as pd


class Solution:
    def __init__(self):
        self.data = pd.read_csv('data/train.csv')
        print(self.data.head())

    def preprosses(self):
        y = self.data['Survived']
        X = self.data.drop(columns = ['Survived'])
        

    def knn_learn(self):
        pass

    def mpl_learn(self):
        pass

a = Solution()