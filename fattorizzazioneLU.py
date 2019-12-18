from random import randrange
import sys

#performs the LU reduction on a matrix

def printMatrix(A):
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            x = round(A[i][j],1)
            sys.stdout.write(str(x))
            sys.stdout.write(" ")
        sys.stdout.write("\n")
    sys.stdout.write("\n\n")
A = []
L = []
C = []
n = 5

for i in range(0,n):
    row = []
    lrow = []
    for j in range(0,n):
        row.append(float(randrange(9)+1))
        if i == j:
            lrow.append(float(1))
        else:
            lrow.append(float(0))
    A.append(row)
    L.append(lrow)
print("A:\n")
printMatrix(A)

for k in range(0,n-1):
    for i in range(k+1,n):
        L[i][k] = A[i][k]/A[k][k]
        for j in range(k+1,n):
            A[i][j] = A[i][j] - L[i][k]*A[k][j]
        A[i][k] = 0
print("U:\n")
printMatrix(A)
print("L:\n")
printMatrix(L)
print("Verifica LU:\n")
for i in range(0,n):
    row = []
    for j in range(0,n):
        s = L[i][0]*A[0][j]
        for k in range(1,n):
            s+=(L[i][k]*A[k][j])
        row.append(s)
    C.append(row)
printMatrix(C)