'''import math

x1=int(input("Введите A x="))
y1=int(input("Введите A y="))
x2=int(input("Введите B x="))
y2=int(input("Введите B y="))

distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
print(f"Растояние от точки A до точки B={distance}" )'''


from functools import reduce

coord1 = list(map(int, input('Введите 2 координаты точки A через запятую: ').split(", ")))
coord2 = list(map(int, input('Введите 2 координаты точки B через запятую: ').split(", ")))

def coordRange(coord1, coord2):
    distance = reduce(lambda x, y: (x + y) ** (1 / 2), (map(lambda coord: (coord[1] - coord[0]) ** 2, zip(coord1, coord2))))
    return round(distance, 2)
    
print(coordRange(coord1, coord2))
