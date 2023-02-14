

def decorator_args(name):
    print(name)
    def decorator(func):
        def wrapper(a, b):
            print('до ')
            result = func(a, b)
            print('после ')
            return result

        return wrapper
    return decorator


@decorator_args('test')
def add(a,b):
    print('function add')
    return a+b

r = add(10,10)
print(r)