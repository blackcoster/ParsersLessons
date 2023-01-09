class Animal:
    def __init__(self, name, breed='Без породы') -> None:
        self.name = name
        self.breed = breed

    def __say_breed(self):
        print(self.breed)

cat = Animal('Барсик', 'Сибирский')
cat._Animal__say_breed()
dog = Animal('Тузик')
dog._Animal__say_breed()

