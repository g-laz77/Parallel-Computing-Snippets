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

for i in range(m[0]):
        print(a[i])

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

# b = [[1,6],[0,2]]
# vec = [7,2]
result = LU_factorization(a,m[0])
# result = backward_sub(vec,b,2)
print(result)