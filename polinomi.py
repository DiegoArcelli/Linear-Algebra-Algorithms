from random import randrange

n = 3
p = []
x = randrange(10)
for i in range(0,n):
    p.append(randrange(10))
string = ""
for i in reversed(range(0,n)):
    string += str(p[i]) + "x^" + str(i)
    if i != 0:
        string += " + "
print(string, "x = " + str(x))

#classic method
s = p[0]
pr = 1
for i in range(1,n):
    pr = pr*x
    s += p[i]*pr
print(s)

#ruffuni-horner
s = p[n-1]
for i in reversed(range(0,n-1)):
    s = s*x + p[i]
print(s)