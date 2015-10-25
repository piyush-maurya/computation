__author__ = 'piyush'

k = int(input())
n = []
for i in range(k):
    n.append(int(input()))

def fib(x):
    if x==1 or x==2:
        return 1
    else:
        prev = 0
        prevPrev = 1
        result = 0
        for i in range(2,x+1):
            result = prev + prevPrev
            prev = prevPrev
            prevPrev = result
        return result

for i in range(k):
    x = 1
    while n[i] != len(str(fib(x))):
        x += 1
    print(x)