class MyClass:
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n>0:
            yield n
            n-=1

obj = MyClass(5)
for n in obj.__iter__():
    print(n)

print(next(obj.__iter__()))
print(next(obj.__iter__()))

print(next(obj.__iter__()))

