# 1

import math

def degree_to_radian(a):
    b = a * (math.pi / 180)
    return b

a = int(input("Enter the degree: "))
b = degree_to_radian(a)
print("Radian:", b)

# 2

import math

def trapezoid(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

height = int(input("Enter the height of the trapezoid: "))
base1 = int(input("Enter the first base of the trapezoid: "))
base2 = int(input("Enter the second base of the trapezoid: "))
area2 = trapezoid(base1, base2, height)
print("Area of trapezoid:", area2)

# 3

import math

def polygon(n, a):
    if n == 4:
        area = a ** 2
        return area
    else:
        area = (n * a ** 2) / (4 * math.tan(math.pi / n))
        return area

n = int(input("Enter the number of sides of the polygon: "))
a = int(input("Enter the side length of the polygon: "))
area = polygon(n, a)
print("Area of polygon:", area)

# 4

import math

def parallelogramm(h, a):
    area = h * a
    return area

h = int(input("Enter the height of the parallelogram: "))
a = int(input("Enter the base length of the parallelogram: "))
area = parallelogramm(h, a)
print("Area of parallelogram:", area)
