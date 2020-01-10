from random import randrange
import sys
import math

#transforms a matrix A in an ortogonal matrix Q using gram-shmidt algorithm
#the best part is that it's so numerically unstable that basically it always
#gives a Q matrix that is useless for anything
#(unless you're lucky enough to get only perfect squares)

def printMatrix(A):
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            x = round(A[i][j],5)
            sys.stdout.write(str(x))
            sys.stdout.write(" ")
        sys.stdout.write("\n")
    sys.stdout.write("\n\n")

def dotProduct(a,b):
    if len(a) == len(b):
        s = 0
        for i in range(0,len(a)):
            s += a[i]*b[i]
        return s

def norm(a):
    s = 0
    for i in range(0,len(a)):
        s += a[i]*a[i]
    return math.sqrt(s)

A = []
Q = []
n = 3

for i in range(0,n):
    row = []
    qrow = []
    for j in range(0,n):
        row.append(float(randrange(9)+1))
        qrow.append(0.0)
    A.append(row)
    Q.append(qrow)

print("A:")
printMatrix(A)
for i in range(0,n):
    temp = []
    for j in range(0,n):
        temp.append(A[j][i])
    for j in range(0,i):
        q_temp = []
        for k in range(0,n):
            q_temp.append(Q[k][j])
        prod = dotProduct(q_temp,temp)/dotProduct(q_temp,q_temp)
        for k in range(0,n):
            q_temp[k] *= prod
            temp[k] -= q_temp[k]
    na = norm(temp)
    for j in range(0,n):
        temp[j] = temp[j]/na
        Q[j][i] = temp[j]
print("Q:")
printMatrix(Q)

