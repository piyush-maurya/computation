__author__ = 'piyush'

k = int(input())
n = []
for i in range(k):
    n.append(int(input()))
for i in range(k):
    x = int(((8*n[i]+1)**(.5)-1)/2)
    if (x*(x+1)>>1)  == n[i]:
        print(x)
    else:
        print(-1)