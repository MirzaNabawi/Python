from math import *
def getrealnumbers(value):
		while True:
			try:
				return float(input(value))
			except ValueError:
				print("Invalid Input!")

CP = getrealnumbers("Enter Current Price: ")
R = getrealnumbers("Yearly Inflation Rate: ")
N = getrealnumbers("Future Year: ")
Y = getrealnumbers("Current Year: ")

FP = CP*((1+R)**(N-Y))

print("If Inflation rate is %.4f%%, then bread will cost $%.2f in %d" % (R, FP ,N))

