def get_real_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("The value is invalid")




a = get_real_number("Enter first number: ")
b = get_real_number("Enter second number: ")
c = get_real_number("Enter third number: ")
d = get_real_number("Enter fourth number: ")

if a>=b and a>=c and a>=d:
    print("Highest Valueis:", a)
elif a>=b and a>=c and a>=d:
    print("Highest Value is:", b)
elif a>=b and a>=c and a>=d:
    print("Highest Value is: ", c)
else: 
    print("Highest Value is: ", d)

if a<=b and a<=c and a<=d:
    print("Lowest Value is: ", a)   
elif a<=b and a<=c and a<=d:
    print("Lowest Value is: ", b)
elif a<=b and a<=c and a<=d:
    print("Lowest Value is: ", c)
else:
    print("Lowest Value is: ", d)


Highest_Value = max(a,b,c,d)
Lowest_Value = min(a,b,c,d)

Average = (Highest_Value + Lowest_Value)/2

print("The Average of the Highest and Lowest Value is: ", Average)  

