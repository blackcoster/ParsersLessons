class ProstoKlass():
    def __call__(self):
        print('меня можно вызвать без метода')
    def say(self):
        print('say')

obj=ProstoKlass()
# obj.__call__()
obj()