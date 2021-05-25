import multiprocessing
import concurrent.futures as cf
from Solution import Solution
import time


class MultiStream(Solution):
    def learn(self):
        start = time.perf_counter()
        with cf.ThreadPoolExecutor(max_workers=3) as e:
            e.submit(self.knn_learn())
            e.submit(self.mlp_learn())
            e.submit(self.linear_learn())
        final = time.perf_counter()
        return final - start
    def get_type(self):
        return 'multistreaming'
