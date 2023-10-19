import math

h = float(input('input the height of the cylinder: '))
r = float(input('Input the radius of the cylinder: '))
PI = math.pi
base_area = 2 * PI * (r ** 2)
lateral_area = (2 * PI * r) * h
surface_area = base_area + lateral_area
print(f'The surface area of this cylinder is: {surface_area}')

