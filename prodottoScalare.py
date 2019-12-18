from random import randrange

#dot product

n = 5
v = []
w = []
for i in range(0,n):
    v.append(randrange(100))
    w.append(randrange(100))
print(v)
print(w)
s = v[0]*w[0]
for i in range(1,n):
    s+=v[i]*w[i]
print(s)