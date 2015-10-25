__author__ = 'piyush'

k = int(input())

def fact(x):
    if x==0 or x==1:
        return 1
    else:
        prev = 1
        result = 0
        for i in range(2,x+1):
            result = i*prev
            prev = result
        return result

for i in range(10,k+1):
    count = 0
    for j in str(i):
        print(j)
        break
