import pandas as pd
import numpy as np
import pickle
import time
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.preprocessing import OneHotEncoder


class Solution:
    def __init__(self):
        self.data = pd.read_csv('data/train.csv', index_col='PassengerId')
        self.models = [None, None, None]
        self.accuracy = [None, None, None]

    def preprosses(self):
        y = self.data['Survived']
        X = self.data.drop(columns=['Survived', 'Ticket', 'Name', 'Cabin'])
        categorical_features = ['Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']
        ohe = OneHotEncoder()
        temp = ohe.fit_transform(X[categorical_features])
        temp = pd.DataFrame(temp.toarray()[1:])
        X.index -= 1
        X = pd.concat((X.drop(columns=categorical_features), temp), axis=1)

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def learn(self):
        pass

    def knn_learn(self):
        model = KNeighborsClassifier(n_neighbors=5)
        for i in range(23):
            self.X_train.loc[self.X_train[i].isna(), i] = 0
        model.fit(self.X_train, self.y_train)
        self.accuracy[0] = model.score(self.X_test, self.y_test)
        self.models[0] = model
        pickle.dump(model, open('models/KNN.sav', 'wb'))

    def mlp_learn(self):
        model = MLPClassifier(hidden_layer_sizes=(150, 50), max_iter=10000)
        for i in range(23):
            self.X_train.loc[self.X_train[i].isna(), i] = 0
        model.fit(self.X_train, self.y_train)
        self.accuracy[1] = model.score(self.X_test, self.y_test)
        self.models[1] = model
        pickle.dump(model, open('models/MLPNN.sav', 'wb'))

    def linear_learn(self):
        model = LogisticRegression()
        for i in range(23):
            self.X_train.loc[self.X_train[i].isna(), i] = 0
        model.fit(self.X_train, self.y_train)
        self.accuracy[2] = model.score(self.X_test, self.y_test)
        self.models[2] = model
        pickle.dump(model, open('models/LinReg.sav', 'wb'))

    def run(self):
        self.preprosses()

        duration = self.learn()

        final_model = VotingClassifier(estimators=[
            ('knn', self.models[0]),
            ('nn', self.models[1]),
            ('log_reg', self.models[2])
        ],
            voting='soft')
        final_model.fit(self.X_train, self.y_train)
        return final_model.score(self.X_test, self.y_test), duration

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
