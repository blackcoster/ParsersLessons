def decorator(func):
    def inner(*args):
        print('start decorator')
        func(*args)
        print('end decorator')
    return inner

@decorator
def say(*args):
    print('hello',args)

# say1 = decorator(say)
# say1()
say('yana','polina','danya')
