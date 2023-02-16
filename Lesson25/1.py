from functools import wraps

def decor(func):
    @wraps(func)
    def wrapper(a,b):
        k = func(a,b)
        return k
    return wrapper


@decor
def func(a,b):
    """Функция, складывающая два числа"""
    return a+b



print(func(3,4))
print(func.__name__)
print(func.__doc__)