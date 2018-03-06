from householder import house
def prod(beta, v):
    vvt = list()
    I = list()
    result = list()
    for i in range(len(v)):
        vvt.append([beta*v[i]*v[j] for j in range(len(v))])
        I.append([0 for j in range(len(v))])
        result.append([0 for j in range(len(v))])
        
    for i in range(len(v)):
        I[i][i] = 1
        for j in range(len(v)):
            result[i][j] = I[i][j] - vvt[i][j]
    return result

def myqr(A, m, n):
    for j in range(0,n):
        # print(A[j:m][j])
        k = []
        for i in range(j,m):
            k.append(A[i][j])
        
        beta,V = house(k)
        ibvvt = prod(beta,V)
        c1 = 0
        for i in range(j,m):
            c2 = 0
            for k in range(j,n):
                A[i][k] *= ibvvt[c1][c2]
                c2 += 1
            c1 += 1
        if j < m:
            count = 1
            for i in range(j+1,m):
                A[i][j] = V[count]
                count += 1
    return A

A = [[1,2],
     [4,5],
     [7,8]]
n = 2
m = 3


print(myqr(A,m,n))