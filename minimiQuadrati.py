import numpy as np
import matplotlib.pyplot as plt

# performs a linear regression analysis on n random
# points by computing the projection matrix

n = 20
points = []
for _ in range(0, n):
    points.append((np.random.randint(0, 100), np.random.randint(0, 100)))

print(points)
A = np.zeros(shape=(n, 2))
b = np.zeros(shape=(n, 1))

for i in range(0, n):
    A[i, 0] = 1
    A[i, 1] = points[i][0]
    b[i] = points[i][1]

print(A)
print(b)

A_n = np.matmul(A.transpose(), A)
p = np.matmul(A.transpose(), b)
x = np.linalg.solve(A_n, p)
print(x)

t = np.linspace(0, 100, 100)
y = x[0] + t*x[1]


plt.plot(A[:, 1], b, 'ro')
plt.axis([0, 100, 0, 100])
plt.plot(t, y, '-b')
plt.show()
