__author__ = 'piyush'

x = int(input())
n = []
a = []
for i in range(x):
    n.append(int(input()))
    for j in range(n[i]):
        a.append([int(k) for k in input().split()])
for i in range(x):
    sum = 0
    for j in range(n[i]):
        max = 0
        for k in range(j+1):
            if max < a[j][k]:
                max = a[j][k]
        sum += max
    print(sum)




