__author__ = 'piyush'

x = int(input())
n = []

for i in range(x):
    n.append(int(input()))

a = [[]]

for i in range(x):
    for j in range(n[i]):
        print(n)
        for k in range(j+1):
            a[j].append(int(input()))
        print(a)


print(a)
