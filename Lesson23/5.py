class Decorator:
    def __init__(self,func):
        print('метод инит')
        self.func = func

    def __call__(self):
        print('начало')
        self.func()
        print('конец')

@Decorator
def smol():
    print('прив')

smol()
# a = Decorator(smol)
# a()