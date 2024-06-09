
import math

def calculate_interest():
    """
    This program calculates either simple or compound interest based on user input.

    The user is told to choose between an investment or a bond. For investment, 
    they input the  amount, interest rate, years, and type of interest (simple 
    or compound). For bond, they input the total household amount, interest rate, 
    and the number of months for repayment.

    Returns:
    None
    """

print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")

# Requesting the user to choose an option between investment or bond
Finance = input("Select the option from the above menu to proceed, 'Investment' or 'Bond': ").strip().capitalize()

# Statement for when the user chooses option or bond
if Finance != 'Investment' and Finance != 'Bond':
    print("Please select a correct option.")
else:
    # calculation for if the user chooses investment 
    if Finance == 'Investment':
        Investment_amount = int(input("Enter the amount of money to deposit: "))
        Investment_interest  = float(input("Enter the percentage for the investment: "))
        Investment_Years = int(input("Enter the years for the investment: "))
        Interest = input("Enter the type of interest you are interested in, 'Simple' or 'Compound' interest: ").strip().capitalize()

        Simple_Interest = Investment_amount * (1 + ((Investment_interest/100) * Investment_Years))
        Compound_Interest = Investment_amount * math.pow((1 + Investment_interest/100), Investment_Years)

        if Interest == 'Simple':
            print(Simple_Interest)
        elif Interest == 'Compound':
            print(Compound_Interest)
        else:
            print ("Please choose the correct option for interest type.")

    # Calculate the bond      
    elif Finance == 'Bond':
        Bond_value = float(input("Enter the total household amount: "))
        Bond_interest = float(input("The interest rate for the house: "))
        Bond_month = int(input("Enter the number of months for the repayment of the bond: "))
        # Calculating the bond formula
        repayment = float((Bond_interest /100)* Bond_value) / (1-(1+ (Bond_interest/100)) ** (-Bond_month))
        print(repayment)