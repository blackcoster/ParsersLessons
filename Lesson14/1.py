def get_name(name='Иван'):
    print(name)

get_name()
get_name('Петр')


class Car:
    def __init__(self, speed, color='Yellow'):
        self.speed = speed
        self.color = color

car1 = Car(100)
car2 = Car(90, 'Blue')

print(f'{car1.color=}')
print(f'{car2.color=}')

