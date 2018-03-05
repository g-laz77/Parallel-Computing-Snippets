import random
m = input("Enter the dimensions of the A matrix followed by bandwidths(lower & upper):").split()
n = input("Enter the dimensions of the B matrix followed by bandwidths(lower & upper):").split()

for i in range(4):
    m[i] = int(m[i])
    n[i] = int(n[i])

c = list()
banded_a = list()
banded_b = list()

for i in range(m[0]):
    banded_a.append([])
    for j in range(m[2]+m[3]+1):
        banded_a[i].append(0)

# print(banded_a)
for i in range(m[0]):
    for j in range(m[1]):
        if not i > j + m[2] and not j > i + m[3]:
            banded_a[i][j-i+m[2]] = random.randint(1,9)

for i in range(n[0]):
    banded_b.append([])
    for j in range(n[2]+n[3]+1):
        banded_b[i].append(0)

for i in range(n[0]):
    for j in range(n[1]):
        if not i > j + n[2] and not j > i + n[3]:
            banded_b[i][j-i+n[2]] = random.randint(1,9)
            
#print (banded_a)
for i in range(m[0]):
    print(banded_a[i])

#print (banded_b)
for i in range(n[0]):
    print(banded_b[i])

if not m[1] == n[0]:
    print("Incompatible operation")
else:
    for i in range(m[0]):
        c.append([])        
        for j in range(n[1]):  
            temp = 0
            for k in range(n[0]):
                if not k > j + n[2] and not j > k + n[3] and not i > k + m[2] and not k > i + m[3]:
                    temp += banded_a[i][k-i+m[2]]*banded_b[k][j-k+n[2]]
            c[i].append(temp)
    print("soln: ")
    for i in range(m[0]):
        print(c[i])
