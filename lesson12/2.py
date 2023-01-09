class Person:
    name = 'Иван'
    age = '11'

    def say(self):
        print('Hello')

circle = [3,5,10]

class Circle:
    x = 0
    y = 0
    r = 1

    def __init__(self,x,y,r):
        self.x = x;
        self.y = y;
        self.r = r;

    def __str__(self):
        return ('Это круг, координаты и радиус:' + str(krug1.x))

krug1 = Circle(11,30,5)
krugdan = Circle(3,8,90)


print(krug1)





