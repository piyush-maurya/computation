__author__ = 'piyush'

k = int(input())

def fib(x):
    f0 = 2
    f1 = 8
    sum = 0
    while f1 <= x:
        sum += f1
        f2 = 4*f1+f0
        f0 = f1
        f1 = f2
    return sum+2

n = []
for i in range(k):
    n.append(int(input()))

for i in range(k):
    print(fib(n[i]))