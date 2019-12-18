from random import randrange
import sys

#it calculates the determinant of a  randomly generated matrix using the gaussian elimination

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
n = 100

for i in range(0,n):
    row = []
    lrow = []
    for j in range(0,n):
        row.append(float(randrange(9)+1))
        lrow.append(float(0))
    A.append(row)
    L.append(lrow)
print("\n")
printMatrix(A)

for k in range(0,n-1):
    for i in range(k+1,n):
        L[i][k] = A[i][k]/A[k][k]
        for j in range(k+1,n):
            A[i][j] = A[i][j] - L[i][k]*A[k][j]
        A[i][k] = 0
s = 1
for i in range(0,n):
    s *= A[i][i]
print("Determinante: " + str(s))