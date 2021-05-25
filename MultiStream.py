import multiprocessing
import concurrent.futures as cf
from Solution import Solution

class MultiStream(Solution):
    def learn(self):
        p1 = multiprocessing.Process(target=self.knn_learn())
        p2 = multiprocessing.Process(target=self.mlp_learn())
        p3 = multiprocessing.Process(target=self.linear_learn())

        p1.start()
        p2.start()
        p3.start()

        p1.join()
        p2.join()
        p3.join()

        # while p1.is_alive() or p2.is_alive() or p3.is_alive():
        #     pass
        # with cf.ThreadPoolExecutor(max_workers=3) as e:
        #     e.submit(self.knn_learn,self)
        #     e.submit(self.mlp_learn,self)
        #     e.submit(self.linear_learn,self)

    def get_type(self):
        return 'multistreaming'