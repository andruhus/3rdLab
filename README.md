# Third lab

This is my 3rd laboratory work where we are comparing one streaming vs multistreaming programming


## Introduction

The task on which I conducted the experiment is a famous [titanic problem](https://www.kaggle.com/c/titanic) where we need to train a model which predicts whether the passenger survived or not

## Project Structure
There is one parent class Solution, which contains common components and two child classes OneStream and MultiStream where we override the learn method

## OneStream 

### Code

```python
class OneStream(Solution):
    def learn(self):
        start = time.perf_counter()
        self.knn_learn()
        self.mlp_learn()
        self.linear_learn()
        final = time.perf_counter()
        return final - start
```

### Results

```bash
We conducted one stream procedure for 1.157677 second(s) and got such an accuracy: 0.698324
The partial accuracies are:
KNN: 0.664804469273743
MLPClassifier: 0.7094972067039106
Linear Model: 0.6368715083798883
```

## MultiStream

### Code

```python
class MultiStream(Solution):
    def learn(self):
        start = time.perf_counter()
        with cf.ThreadPoolExecutor(max_workers=3) as e:
            e.submit(self.knn_learn())
            e.submit(self.mlp_learn())
            e.submit(self.linear_learn())
        final = time.perf_counter()
        return final - start
```

### Results

```bash
We conducted multistreaming procedure for 0.945669 second(s) and got such an accuracy: 0.692737
The partial accuracies are:
KNN: 0.664804469273743
MLPClassifier: 0.6759776536312849
Linear Model: 0.6368715083798883
```

## Сonclusions

As we can see multiprocessing can help with this or similar types of problems. In our case the difference may look insignificant but as the dataset grow larger the performance will show better results

