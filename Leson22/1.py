def decorator(func):
    def wrapper():
        print('функция-обертка')
        func()
    return wrapper


def basic():
    print('основная функция')

wrapped = decorator(basic)

print('старт программы')
wrapped()
print('конец программы')