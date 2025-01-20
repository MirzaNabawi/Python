#taking real numbers as input
from math import *
def getrealnumbers(value):
    while True:
        try:
            return float(input(value))
        except ValueError:
            print("Please enter a real number")


#taking input from user
punch_amount = getrealnumbers("Enter the punch capacity: ")
glass_capacity = getrealnumbers("Enter the glass capacity: ")

#convert the capacity of glasses to litres
#since 33.8140226 Ounces = 1 litre
#so

glass_capacity = glass_capacity/33.8140226

#calculate the number of glasses required

number_of_glassses_required = punch_amount//glass_capacity

print("The number of glasses required are: ", number_of_glassses_required)

#calculate the remaining punch

punch_remaining = punch_amount%glass_capacity
punch_remaining = punch_remaining*33.8140226
print("The remaining punch is: ", punch_remaining)


