from math import *
def realnumbers(value):
    while True:
        try:
            return float(input(value))
        except ValueError:
            print

a = realnumbers("Enter the first side of the triangle: ")
b = realnumbers("Enter the second side of the triangle: ")
c = realnumbers("Enter the third side of the triangle: ")

s = (a+b+c)/2
area = sqrt(s*(s-a)*(s-b)*(s-c))

print("The area is ", area, "cm sqared units")