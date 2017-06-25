# A program that calculates the amount of penies earned if doubled per day
# 19 June 2017
# CTI-110 M4HW2 - Pennies for Pay
# Ekow Yawson
#


#In this program, I McGuyvered it
print('This program will calculate the amount of money a person would earn')
print('over time if the salary was one penny the first day and doubled')
print('each consecutive day.\n')

# define total number of days,
# and the total pennies counter
days = int(input('Input number of days worked: '))
pennies_counter = 0

print('Day\tPennies Earned')
print('---\t--------------')
# specify for loop, define input as days, and define pennies earned.
for current_day in range(days):
    pennies_earned = 2 ** current_day
    pennies_counter += pennies_earned
    print(current_day + 1, '\t', pennies_earned)
    

print('\nTotal in dollar amount: $', format(pennies_counter * 0.01, ',.2f'), sep = '')
input('\nPress Enter to exit.')
