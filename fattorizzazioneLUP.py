from random import randrange
import sys

#performs the LU reduction with partial pivoting on a matrix

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
P = []
n = 4

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
    P.append(i)
P.append(n)

'''A = []
A.append([2,1,5])
A.append([4,4,-4])
A.append([1,3,1])'''

'''A = []
A.append([2,5,9,3])
A.append([9,9,7,9])
A.append([1,4,8,9])
A.append([6,9,3,6])'''

print("A:\n")
printMatrix(A)

for k in range(0,n-1):
    i_max = k
    v_max = abs(A[k][k])
    for i in range(k+1,n):
        t=abs(A[i][k])
        if(t > v_max):
            v_max = t
            i_max = i
    if k != i_max:
        tp = P[k]
        P[k] = P[i_max]
        P[i_max] = tp
        P[n]+=1
        for j in range(k,n):
            swap = A[k][j]
            A[k][j] = A[i_max][j]
            A[i_max][j] = swap
        if k != 0:
            for j in range(0,min(i_max,k)):
                tl = L[k][j]
                L[k][j] = L[i_max][j]
                L[i_max][j] = tl
    for i in range(k+1,n):
        L[i][k] = A[i][k]/A[k][k]
        for j in range(k+1,n):
            A[i][j] = A[i][j] - L[i][k]*A[k][j]
        A[i][k] = 0

print("U:\n")
printMatrix(A)
print("L:\n")
printMatrix(L)
print("P:\n")
print(P)
print("\nVerifica PA = LU:\n")
for i in range(0,n):
    row = []
    for j in range(0,n):
        s = L[i][0]*A[0][j]
        for k in range(1,n):
            s+=(L[i][k]*A[k][j])
        row.append(s)
    C.append(row)
'''for i in range(0,n):
    if(P[i] != i):
        for j in range(0,n):
            t = C[P[i]][j]
            C[P[i]][j] = C[i][j]
            C[i][j] = t'''
printMatrix(C)