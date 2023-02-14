class Decorator:

    def __init__(self,name):
        print('name')
        self.name = name

    def __call__(self,func):
        def wrapper(a,b):
            print('до')
            func(a,b)
            print('после')
        return wrapper


@Decorator('test')
def add(a,b):
    print('вот ваши числа',a,b)

add(10,10)