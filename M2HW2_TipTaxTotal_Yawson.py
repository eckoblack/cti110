#A program that calcualates the total amount of a meal purchased at a restaurant
#9 June 2017
#CTI-110 M2HW2 - Tip Tax Total
#Ekow Yawson


#User input of charge for food purchased
purchase_charge = float(input("Input the initial charge for food purchased\
                              \nUse the following format -- xx.xx: "))

#calculate 18% tip, 7% tax, and total
tip = 0.18 * purchase_charge
tax = 0.07 * purchase_charge
total = purchase_charge + tip + tax

#output total charge with tip and tax included
print("The tip amount is", (format(tip, '12,.2f')))
print("The tax amount is", (format(tax, '12,.2f')))
print("The total amount is", (format(total, '10,.2f')))
input("Press Enter to exit.")
