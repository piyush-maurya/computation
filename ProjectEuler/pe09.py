__author__ = 'piyush'

k = int(input())

n = []
for i in range(k):
    n.append(int(input()))



def pyth(x):
    p = []
    for a in range(1,x>>1):
        b = int((x**2-2*x*a)/(2*x-2*a))
        c = x-a-b

        if (a**2+b**2) == c**2:
            p.append(int(a*b*c))
    if not p:
        return -1
    else:
        return max(p)

for i in range(k):
    print(pyth(n[i]))