class Person:
   def __init__(self, name):
       self.name = name

   def __str__(self):
       return f'Меня зовут {self.name}'
       #return ('меня зовут'+self.name)

person1 = Person('Иван')
print(person1)