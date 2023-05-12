from math import pi


def circle_area(radius):
    if type(radius) not in [int,float]:
        raise TypeError('введите число')
    if radius<0:
        raise ValueError('Радиус должен быть неотрицательным')
    return pi*radius**2

# print(circle_area('five'))
# r_list = [2,0,-3,2+3j,True,[2,5],'seven']
#
# for r in r_list:
#     s = circle_area(r)
#     print(f'радиус {r} площадь {s}')