class Car:
    def __init__(self, speed, color='Yellow', owner=None) :
        self.speed = speed
        self.color = color
        self.owner = owner

    def say_owner(self):
        if self.owner:
            print(f'Владелец {self.owner}')
        else:
            print('У данного автомобиля нет владельца')


car1 = Car(100, 'green', 'Иван')
car2 = Car(90,color = 'blue',owner='polina')
car1.say_owner()
car2.say_owner()
