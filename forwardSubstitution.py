from random import randrange

#performs a forward substitution algorithm in a upper triangular matrix randomly generated


A = []
b = []
x = []
n = 3

for i in range(0,n):
    row = []
    b.append(float(randrange(9)+1))
    x.append(float(0))
    for j in range(0,n):
        if i > j:
            row.append(float(0))           
        else:
            row.append(float(randrange(9)+1))
    A.append(row)
    print(A[i])
print("\n")
print(b)

for i in range(0,n):
    s = b[i]
    for j in range(0,i-1):
        s = s - A[i][j]*x[j]
    x[i] = s/A[i][i]

print("\nSoluzione:")
print(x)