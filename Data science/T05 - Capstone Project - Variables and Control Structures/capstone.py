import math
'''
Capstone Project
For this Capstone Project, assume that you have been approached by a small
financial company and asked to create a program that allows the user to access
two different financial calculators: an investment calculator and a home loan
repayment calculator.
'''

while True:
    print("""
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
""")
    # this will get the user to input which financial calculations they would like to calculate
    selection = input("""Enter either 'investment' or 'bond' from the menu above to proceed : 
                      type in exit to terminate: """).lower()

    if selection == 'investment':
        # P = The amount deposited
        P = float(input("Please enter the amount you would like to deposit : "))
        # r = Rate of interest (%) user shouldn't add the % symbol to input
        r = float(input("Please enter the rate of interest (exclude % symbol) : ")) / 100
        # t = amount of years of investment
        t = int(input("Please enter the years for investment : "))

        # this will ask the user if they cal simple or compound interest
        calculation_selection = input("Please select either simple or compound interest : ").lower()

        # this calculates total amount  after simple interest
        if calculation_selection == 'simple':
            A = P * (1 + r * t)
            print(f"The total amount after simple interest is: {A:.2f}")
            continue

        # this will calculate the total amount after compound interest
        elif calculation_selection == 'compound':
            A = P * math.pow((1 + r), t)
            print(f"The total amount after compound interest is: {A:.2f}")
            continue
        #this will print an error message due to invalid selection
        else:
            print("Invalid selection")
            continue
    # asking user to imput  relevant information regarding the bond
    elif selection == 'bond':
        P = float(input("Enter the present value of your house : "))
        r = float(input("Please enter the annual rate of interest (exclude % symbol) : ")) / 100 / 12
        n = int(input("Please enter the number of months planned for repayment : "))
        
        #this calculate and print the bond repayment 
        repayment = (r * P) / (1 - math.pow(1 + r, -n))
        print(f"The monthly bond repayment amount is: {repayment:.2f}")
        continue

    elif selection == 'exit':
        print("Exiting. . . ")
        break

    else:
        print('Invalid input')
