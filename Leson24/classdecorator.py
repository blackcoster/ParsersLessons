import datetime

def timer(cls):
    def wrapper():
        start = datetime.datetime.now()
        result = type(cls)
        end = datetime.datetime.now()
        print(result)
        return result
    return wrapper

@timer
class Myclass:
    pass

obj = Myclass()

