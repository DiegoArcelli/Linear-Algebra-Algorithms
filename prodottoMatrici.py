from random import randrange

#matricies product

n = 3
l = 4
m = 2
A = [] 
B = [] 
C = []

for i in range(0,m):
    row = []
    for j in range(0,l):
        row.append(randrange(10))
    A.append(row)
    print(A[i])
print("\n")
for i in range(0,l):
    row = []
    for j in range(0,n):
        row.append(randrange(10))
    B.append(row)
    print(B[i])
print("\n")
for i in range(0,m):
    row = []
    for j in range(0,n):
        s = A[i][0]*B[0][j]
        for k in range(1,l):
            s+=(A[i][k]*B[k][j])
        row.append(s)
    C.append(row)
    print(C[i])