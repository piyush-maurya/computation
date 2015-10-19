# Program for calculating fibonacci series.
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

y = int(raw_input('enter number:'))
print(fib(y))
