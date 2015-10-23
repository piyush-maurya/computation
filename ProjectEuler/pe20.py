__author__ = 'piyush'

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

k = int(input())
x = []
for i in range(k):
    x.append(int(input()))

for i in range(k):
    sum = 0
    for j in str(fact(x[i])):
        sum += int(j)
    print(sum)