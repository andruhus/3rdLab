from Solution import Solution
import time


class OneStream(Solution):
    def learn(self):
        start = time.perf_counter()
        self.knn_learn()
        self.mlp_learn()
        self.linear_learn()
        final = time.perf_counter()
        return final - start

    def get_type(self):
        return 'one stream'
