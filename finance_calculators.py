"""
start:
1. import math (not used in this code but requested in task instructions)
2. prompt the user to input investment or bond
    unify capitalisation of the input
3. if: 
    3.1 investment: 
        prompt user to input amount(P), 
        prompt user to input interest rate(r) 
        prompt user to input years(t) 
        ask user to choose compounding or simple:
            3.1.1 if compounding:
                set variable total_comp as P(1+r/100)**t
                print total
            3.1.2 elif simple:
                set variable total_simp as P*(1+r/100*t)
                print total
            3.2.3 else print Error
    3.2 elif bond:
        prompt user to input value(P)
        prompt user to input interest rate(i) = input/100/12
        prompt user to input months(n)
        calculate repayment = (i*P)/(1-(1+i)**(-n))
        print repayment
    3.3 else:
        print Error
                
"""
import math

print("investment - calculate the amount of interest you'll earn on your investment.\nbond - calculate the amount you'll have to pay on a home loan\nEnter 'investment' or 'bond' to proceed:")
option = input().lower()

if option == 'investment':
    amount = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (numbers only, please do not enter %): ")) / 100
    years = int(input("Enter the number of years you plan on investing: "))
    interest_type = input("Choose interest by entering 'simple' or 'compound': ").lower()

    if interest_type == 'simple':
        investment_with_interest = amount * (1 + interest_rate * years)
    elif interest_type == 'compound':
        investment_with_interest = amount * (1 + interest_rate) ** years
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        exit()

    print(f"The total amount after {years} years will be: {investment_with_interest:.2f}")

elif option == 'bond':
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the annual interest rate (numbers only, please do not enter %): ")) / 100
    months = int(input("Enter the number of months for repayment: "))

    repayment = (interest_rate / 12 * present_value) / (1 - (1 + interest_rate / 12) ** -months)

    print(f"The monthly bond repayment will be: {repayment:.2f}")

else:
    print("Invalid option. Please enter 'investment' or 'bond'.")
