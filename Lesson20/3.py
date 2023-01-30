numbers = [1,2,[3,[4,5],6,7],8]

def func(n):
    for i in n:
        if isinstance(i,list):
            yield from func(i)
        else:
            yield i

