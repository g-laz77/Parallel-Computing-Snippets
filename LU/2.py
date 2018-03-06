import copy
import random

m = input("Enter the dimensions of the A matrix:").split()
for i in range(2):
    m[i] = int(m[i])

a = list()
# Lower Triangular matrix
for i in range(m[0]):
    a.append([0 for j in range(m[1])])
    # a[i] = list()
    for j in range(m[1]):
        # if j<=i:
            a[i][j] = random.randint(1,9)

# for i in range(m[0]):
#         print(a[i])

def forward_sub(B, A, n):
    B[0] = B[0]/A[0][0] 
    for i in range(1,n):
        temp = 0;
        for j in range(0,i):
            temp += A[i][j]*B[j] 
        # print(temp,B[i])
        B[i] = (B[i] - temp)/A[i][i]
    return B

def backward_sub(B, A, n):
    B[n-1] = B[n-1]/A[n-1][n-1] 
    for i in range(n-2,-1,-1):
        temp = 0;
        for j in range(i+1,n):
            temp += A[i][j]*B[j] 
        B[i] = (B[i] - temp)/A[i][i]
    return B

def LU_factorization(A,n):
    for k in range(0,n-1):
        for l in range(k+1,n):
            A[l][k] = A[l][k]/A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j] = A[i][j] - A[i][k]*A[k][j]
        
    return A

def mult_vec(A,X,n):
    b = [0 for i in range(n)]
    for i in range(n):
        temp = [A[i][j]*X[j] for j in range(n)]
        for k in temp:
            b[i] += k
    return b

def lu_solve(A,n,B):
    L = copy.deepcopy(A)
    U = copy.deepcopy(A)
    for i in range(n):
        L[i][i] = 1
        for j in range(n):
            if j>i:
                L[i][j] = 0
            if j<i:
                U[i][j] = 0
    print("L:\n")
    for i in range(n):        
        print(L[i])
    print("\nU:\n")
    for i in range(n):        
        print(U[i])
    print("\nA:\n")
    for i in range(n):        
        print(a[i])
    print("\n")
    T = forward_sub(B,L,n)
    X = backward_sub(T,U,n)
    print("X: ", X,"\n")
    act_X = mult_vec(a, X, n)
    print("Recalculated B: ", act_X)
    # print(act_X)

a = [[3,5],[6,7]]
vec = [9,4]
copy_a = copy.deepcopy(a)
result = LU_factorization(copy_a,2)
lu_solve(result,m[0],vec)
# result = backward_sub(vec,b,2)
# for i in range(m[0]):
#     print(result[i])