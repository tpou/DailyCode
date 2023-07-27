from src.prob import prob1439
import numpy as np

A = [['F','A','C','I'],
     ['O','B','Q','P'],
     ['A','N','O','B'],
     ['M','A','S','S']]
nA = np.array(A)
target = 'CQOS'
print(prob1439(A,target))