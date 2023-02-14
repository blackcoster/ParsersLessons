def repeat(n):
    print(n)
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat(9)
def hello():
    print('hello')

hello()
