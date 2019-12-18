from random import randrange

#triangular matricies product

n = 3
l = 3
m = 3
A = [] 
B = [] 
C = []
T = []

for i in range(0,n):
    row = []
    for j in range(0,n):
        row.append(0)
    T.append(row)

for i in range(0,m):
    row = []
    for j in range(0,l):
        if i <= j:
            row.append(randrange(10))
        else:
            row.append(0)
    A.append(row)
    print(A[i])
print("\n")

for i in range(0,l):
    row = []
    for j in range(0,n):
        if i <= j:
            row.append(randrange(10))
        else:
            row.append(0)
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
    
print("\n")
for i in range(0,n):
    row = []
    for j in range(i,n):
        s = 0
        for k in range(i,j+1):
            s+=(A[i][k]*B[k][j])
        T[i][j]=s
    print(T[i])

print("\n")
