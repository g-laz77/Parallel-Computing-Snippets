import random 
import copy
import math
X = [2, 6, 8]

def house(X):
    m = len(X)
    sigma = 0
    for i in range(1,m):
        sigma += X[i]*X[i] 
    print("sigma:",sigma)
    V = copy.deepcopy(X)
    V[0] = 1
    if not sigma and X[0] >= 0:
        beta = 0
    elif not sigma and X[0] < 0:
        beta = -2
    else:
        mu = math.sqrt(X[0]*X[0]+sigma)
        if X[0] <= 0:
            V[0] = X[0] - mu
        else:
            V[0] = float(-1 * sigma) / (X[0] + mu) 
        beta = float(2 * V[0] * V[0]) / (sigma + V[0]*V[0])
    
    for i in range(len(V)):
        V[i] = V[i]/V[0]
    
    return beta, V

print(house(X))

