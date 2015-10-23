__author__ = 'piyush'

k = int(input())
n = []
for i in range(k):
    n.append(int(input()))

for i in range(k):
    sum = 0
    for j in str(2**n[i]):
        sum += int(j)
    print(sum)