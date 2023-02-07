def decorator(func):
    def a():
        print('---до функции')
        func()
        print('---после функции')
    return a


@decorator
def wrapped():
    print('---- функция')

# a = decorator(wrapped)

wrapped()
