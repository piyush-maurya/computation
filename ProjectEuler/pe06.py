__author__ = 'piyush'

k = int(input())
x = []
for i in range(k):
    x.append(int(input()))
for j in range(k):
    diff = 0
    n = x[j]
    diff = int(((((n*(n+1))/2)**2) - ((n*(n+1)*(2*n+1))/6)))
    print(diff)
