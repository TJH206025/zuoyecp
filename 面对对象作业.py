import math
a=math.pi
class Circle(object):
    def __init__(self,radius):
        self.__radius=radius
    def set_radius(self,radius):
        if radius <0:
            raise Exception("半径必须大于0奥！")
        else:
            self.__radius=radius
    def get_radius(self):
        return self.__radius
    def get_area(self):
        area = a*(self.__radius)**2
        return round(area, 2)
    def get_girth(self):
        girth = 2*a*(self.__radius)
        return round(girth, 2)
mia =Circle(5)
print(mia.get_radius())
mia.set_radius(-5)
print(mia.get_radius())
print(mia.get_area())
print(mia.get_girth())
print(Circle.__dict__)


