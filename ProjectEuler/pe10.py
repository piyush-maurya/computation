__author__ = 'piyush'

def prime(n):
    sum = 0
    for num in range(2,n+1):
        if all(num%i!=0 for i in range(2,num)):
            return num



k = int(input())
n = []
for i in range(k):
    n.append(int(input()))
for i in range(k):
    print(prime(n[i]))
