k = [int(i) for i in input().split()]
n = int(k[0])
m = int(k[1])
a = [[0 for i in range(n)]for j in range(m)]
for i in range(n):
    a[i] = [int(j) for j in input().split()]
for i in range(n):
    for j in range(m):
