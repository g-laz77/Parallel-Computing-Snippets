import random

m = input("Enter the dimensions of the A matrix:").split()
n = input("Enter the dimensions of the B matrix:").split()

for i in range(2):
    m[i] = int(m[i])
    n[i] = int(n[i])

a = list()
b = list()

for i in range(m[0]):
    a.append([random.randint(0,9) for j in range(m[1])])

for i in range(n[0]):
    b.append([random.randint(0,9) for j in range(n[1])])

print(a)
print(b)

c = list()

if not m[1] == n[0]:
    print("Incompatible operation")
else:
    for i in range(m[0]):
        c.append([])        
        for j in range(n[1]):  
            temp = 0
            for k in range(n[0]):
                temp += a[i][k]*b[k][j]
            c[i].append(temp)
    print("soln: ")
    for i in range(m[0]):
        print(c[i])