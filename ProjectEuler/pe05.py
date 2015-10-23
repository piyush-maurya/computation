__author__ = 'piyush'

k = int(input())

x = []
for i in range(k):
    x.append(int(input()))

def prime(a):
    sum = []
    for num in range(2,a+1):
        if all(num%i!=0 for i in range(2,num)):
            sum.append(num)
    return sum

def lcm_upto(N):
  total = 1
  for p in prime(N):
    x=1
    while x*p <= N:
      x=x*p
    total = total * x
  return total

for i in range(k):
    print(lcm_upto(x[i]))