import random

m = input("Enter the dimensions of the A matrix:").split()
for i in range(2):
    m[i] = int(m[i])

a = list()
b = [[1,4,2],[3,4,1],[0,2,3]]

# Hessenberg matrix
for i in range(m[0]):
    a.append([0 for j in range(m[1])])
    for j in range(m[1]):
        if j>=i-1:
            a[i][j] = random.randint(1,9)
print("Hessenberg Matrix A:\n")
for i in range(m[0]):
    print(b[i])

def LU_factorization(A,n):
    for k in range(0,n-1):
        A[k+1][k] = A[k+1][k]/A[k][k]
        for l in range(k+1,n):
            A[k+1][l] = A[k+1][l] - A[k+1][k]*A[k][l]
        
    return A

result = LU_factorization(b,3)
# result = backward_sub(vec,b,2)
print("LU factorization:\n\n")
print(result)

