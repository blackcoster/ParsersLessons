class Decorator:
    def __init__(self,func):
        # print('метод инит')
        self.func = func

    def __call__(self,n):
        print('начало')
        self.func(n)
        print('конец')

@Decorator
def smol(n):
    print('прив',n)

smol('polina')