def decorator(func):
    def inner(n,m):
        print('start decorator')
        func(n,m)
        print('end decorator')
    return inner

@decorator
def say(name,surname):
    print('hello',name, surname)

# say1 = decorator(say)
# say1()
say('yana','polina')