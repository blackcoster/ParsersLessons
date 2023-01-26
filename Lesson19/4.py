def func():
    yield 42
    return 'конец списка'

result = func()
print(result)
print(next(result))
print(next(result))
