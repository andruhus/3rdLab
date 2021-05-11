import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

class Solution:
    def __init__(self):
        self.data = pd.read_csv('data/train.csv',index_col='PassengerId')
        self.models = [None,None,None]
        self.accuracy = [None,None,None]

    def preprosses(self):
        y = self.data['Survived']
        X = self.data.drop(columns = ['Survived','Ticket'])
        categorical_features = ['Pclass','Sex','SibSp','Parch','Embarked']
        X = pd.concat((X, pd.get_dummies(X[categorical_features])), 1)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X,y,test_size=0.2,random_state=42)


    def knn_learn(self):
        model = KNeighborsClassifier(n_neighbors=5)
        model.fit(self.X_train,self.y_train)
        self.accuracy[0] = model.score(self.X_test,self.y_test)
        self.models.append[0] = model
        pickle.dump(model, open('models/KNN.sav','wb'))


    def mpl_learn(self):
        pass

    def linear_model(self):
        pass

    def run(self):
        pass

a = Solution()
a.preprosses()