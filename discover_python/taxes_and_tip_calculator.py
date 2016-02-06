"""
Author: Rick Harris (rickharris-dev)
Program: Taxes and Tip Calculator
Description: This program calculates the tax and tip based on the given
data including price before tax, tax rate (in %), and tip rate (in %).
"""

from decimal import *


#This defines the function name that will be run.
def tax_and_tip_calculator():
    """
    Prompts user for data including price before tax, tax rate (in %),
    and tip rate (in %).

    Returns:
        A value totaling the price before tax, tax and tip rate.
    """

    #Prints the text inside the quotes
    print "Welcome to the taxes and tip calculator!"

    #Prompts for the before tax price and stores it in the price variable
    price = raw_input("What is the price before tax? ")

    #Prompts for the tax rate and stores it in the tax variable
    tax = raw_input("What are the taxes? (in %) ")

    #Prompts for the tip rate and stores it in the tip variable
    tip = raw_input("What do you want to tip? (in %) ")

    #Sets the initial total value as price converted to a float value
    total = float(price)

    #Adds total to the total multiplied by the tax rate
    total += total * float(tax) / 100

    #Adds total to the total multiplied by the tip rate
    total += total * float(tip) / 100

    #Prints the line incorporating the total at %f to format as float decimal
    print "The price you need to pay is: $%f." % (total)

#Ensures the file is being run directly rather than as an import    
if __name__ == '__main__':

    #Initiates the tax_and_tip_calculator defined above.
    tax_and_tip_calculator()
