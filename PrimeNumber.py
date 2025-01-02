from math import sqrt

prime_number = int(input("Enter a number > 1: "))

is_prime_number = True
divisor = 2

while is_prime_number and divisor <= sqrt(prime_number):
     if prime_number % divisor == 0:
          is_prime_number = False
     else:
          divisor += 1

if is_prime_number == True:
     print("This is a Prime Number")
else:
     print("This is not a Prime Number, it is a multiple of ", divisor)
    


                   

                  