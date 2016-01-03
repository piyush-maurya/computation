__author__ = 'piyush'

k = int(input())
x = []
z = []
for i in range(k):
    x.append([int(i) for i in input().split()])
    z.append(int(input()))
for i in range(k):
    sum = 0
    a = list(str(z[i]))
    total = 0
    for j in range((x[i][0]-x[i][1])+1):
        temp = 1
        for l in range(j,j+x[i][1]):
            temp *= int(a[l])
        if total < temp:
            total = temp
    sum += total
    print(sum)