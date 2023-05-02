class CircleRadius():
    def __init__(self,radius):
        self.radius = radius
        self.pi = 3.141

    def getRadius(self):
        return self.radius

    def setRadius(self,radius):
        self.radius = radius


krug = CircleRadius(67)

print(krug.getRadius())

krug.setRadius(54)
print(krug.getRadius())