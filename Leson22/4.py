
def decor(func):
    def wrapper():
        print('начало')
        func()
        print('конец')
    return wrapper
@decor
def smol_func():
    print('привет, мир!')

smol_func()

