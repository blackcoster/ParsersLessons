class MyClass:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


a = MyClass('Ivan')
print(a.name)

a.name = 'Sergey'
print(a.name)

