# Program for calculating fibonacci series.

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1)+fib(x-2)


k = int(input())
print(fib(k))
#for i in range(k+1):
#    print(fib(i))