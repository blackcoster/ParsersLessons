 #1 1 2 3 5 8 13 21 34 55
 #1 2 3 4 5 6 7  8  9  10
def fib(n):
    fib0 = 1
    yield fib0
    fib1 = 1
    yield fib1
    for i in range(n-2):
        fib0,fib1 = fib1,fib0+fib1
        yield fib1

for num in fib(100):
    pass
print(num)


