def get_type(a):
    def wrapper():
        result = a()
        print(type(result))
    return wrapper

@get_type
def func():
    return 4+5

func()