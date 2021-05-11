from Solution import Solution

class OneStream(Solution):
    def learn(self):
        self.knn_learn()
        self.mlp_learn()
        self.linear_learn()