import multiprocessing
from Solution import Solution

class MultiStream(Solution):
    def learn(self):
        p1 = multiprocessing.Process(target=self.knn_learn)
        p2 = multiprocessing.Process(target=self.mlp_learn)
        p3 = multiprocessing.Process(target=self.linear_learn)

        p1.start()
        p2.start()
        p3.start()

        p1.join()
        p2.join()
        p3.join()