def bread(func):
    def wrapper():
        print('хлеб')
        func()
        print('хлеб')
    return wrapper
def ingredients(func):
    def wrapper():
        print('помидоры')
        func()
        print('салатик')
    return wrapper




@bread
@ingredients
def sandwich():
    print('ветчина')

sandwich()