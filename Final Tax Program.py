def real_numbers(value):
    while True:
        try:
            return float (input(value))
        except ValueError:
            print("Invalid Input!")

earnings= real_numbers("Please Enter Your Earnings $: " )



if earnings <= 10000:
    print("No Tax Has been charged")
else:
    if earnings > 10000 and earnings <= 50000:
        first_tax_bracket = (earnings-10000)*(20/100)
        print("Based on your earnings of $%.2f  the taxes are $%.2f " % (earnings, first_tax_bracket))
    elif earnings > 50000:
        first_tax_bracket = (50000 -10000)*(20/100)
        second_tax_bracket = (earnings - 50000)*(30/100)
        final_tax = (first_tax_bracket + second_tax_bracket)
        print("Based on your earnings of $%.2f  the taxes are $%.2f " % (earnings, final_tax))

