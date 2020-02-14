from random import randrange
import numpy as np


# performs the QR reduction on a matrix using householder reflection
# i used numpy for the vectorial operation


n = 5

A = np.identity(n)

for i in range(0, n):
    for j in range(0, n):
        A[i, j] = np.float128(randrange(10))

R = np.copy(A)
print("\nA:")
print(R)
Q = np.identity(n)
Id = np.copy(Q)
for k in range(0, n-1):
    x = np.array(R[:, k])
    for i in range(0, n):
        if i < k:
            x[i] = 0
    e = np.zeros(n)
    e[k] = 1
    u = x - np.linalg.norm(x)*e
    v = u / np.linalg.norm(u)
    Q_temp = Id - 2*np.outer(v, v)
    Q = np.matmul(Q, Q_temp)
    R = np.matmul(Q_temp, R)

print("\n\nQ:")
print(Q)
print("\n\nR:")
print(R)
print("\nVerifica Q*R:")
print(np.matmul(Q, R))
