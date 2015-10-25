__author__ = 'piyush'

k = int(input())
n = []
for i in range(k):
    n.append(int(input()))

def prime(n):
    sum = 0
    for num in range(2,n+1):
        if all(num%i!=0 for i in range(2,num)):
            sum += num
    return sum

print(prime(6))