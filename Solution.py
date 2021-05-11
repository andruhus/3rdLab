import pandas as pd
import pickle
import time
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingClassifier

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

    def learn(self):
        pass

    def knn_learn(self):
        model = KNeighborsClassifier(n_neighbors=5)
        model.fit(self.X_train,self.y_train)
        self.accuracy[0] = model.score(self.X_test,self.y_test)
        self.models.append[0] = model
        pickle.dump(model, open('models/KNN.sav','wb'))

    def mlp_learn(self):
        model = MLPClassifier(hidden_layer_sizes=(150,50))
        model.fit(self.X_train, self.y_train)
        self.accuracy[1] = model.score(self.X_test, self.y_test)
        self.models.append[1] = model
        pickle.dump(model, open('models/MLPNN.sav', 'wb'))

    def linear_learn(self):
        model = LinearRegression()
        model.fit(self.X_train, self.y_train)
        self.accuracy[2] = model.score(self.X_test, self.y_test)
        self.models.append[2] = model
        pickle.dump(model, open('models/LinReg.sav', 'wb'))

    def run(self):
        self.preprosses()
        start = time.perf_counter()
        self.learn()
        final = time.perf_counter()
        final_model = VotingClassifier(estimators=[('knn',self.models[0]),
                                                   ('nn',self.models[1]), ('lin',self.models[2])],
                                       voting='soft')
        final_model.fit(self.X_train,self.y_train)
        return final_model.score(self.X_test,self.y_test),final - start

    def get_type(self):
        pass

    def print_results(self):
        overal_score, overall_time = self.run()
        type = self.get_type()
        print(f'We conducted {type} procedure for {overall_time} second(s) and got such an accuracy: {overal_score}')

    def get_partial_accuracy(self):
        print('The partial accuracies are:')
        print(f'KNN: {self.accuracy[0]}')
        print(f'MLPClassifier: {self.accuracy[1]}')
        print(f'Linear Model: {self.accuracy[2]}')

