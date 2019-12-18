from random import randrange

#vector-matrix product

n = 3
m = 4
A = [] 
b = []
c = []
for i in range(0,m):
    row = []
    for j in range(0,n):
        row.append(randrange(10))
    A.append(row)
    print(A[i])
print("\n")
for i in range(0,n):
    b.append(randrange(10))
print(b)
for i in range(0,m):
    s = A[i][0]*b[0]
    for j in range(1,n):
        s+=A[i][j]*b[j]
    c.append(s)
    s = 0
print("\n")
print(c)