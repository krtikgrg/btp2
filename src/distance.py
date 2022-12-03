import numpy as np

def cosine_s(A,B):
    cosine = np.dot(A,B)/(np.linalg.norm(A)*np.linalg.norm(B))
    return cosine

def cosine_d(A,B):
    return 1-cosine_s(A, B)

def euclidean_d(A,B):
    distance = np.sum((A-B)**2)**0.5    
    return distance

def manhattan_d(A,B):
    return np.sum(abs(A-B))

def minkowski_d(A,B,p):
    return np.sum((abs(A-B))**p)**(1/p)

def jaccard_index(A,B):
    inter = 0
    union = 0
    for i in range(len(A)):
        if A[i] == B[i] and A[i] == 1:
            inter += 1
            union += 1
        elif A[i] != B[i]:
            union += 1
    return (inter/union)