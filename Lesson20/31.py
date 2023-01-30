# def func():
#     while True:
#         n = yield
#         print(n**2)
#
# r = func()
# r.send(None)
# r.send(1)
# r.send(2)
# r.send(6)

def double_number(number):
    while True:
        number*=2
        number = yield number
c = double_number(4)

c.send(None)
for n in range(10):
    n = c.send(n)
    print(n)
