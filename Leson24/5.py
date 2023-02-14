from functools import wraps

def decorator(func):
    """ Декоратор"""
    @wraps(func)
    def wrapper():
        """Вложенная функция"""
        func()
    return wrapper

@decorator
def func():
    """Оборачиваемая функция"""
    print('прив')

# func()
print(func.__doc__)