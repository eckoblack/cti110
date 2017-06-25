# A program that calculates the amount of penies earned if doubled per day
# 19 June 2017
# CTI-110 M4HW2 - Pennies for Pay
# Ekow Yawson
#



# In this program, I followed Tony Gaddis' example:
print('This program will calculate the amount of money a person would earn')
print('over time if the salary was one penny the first day and doubled')
print('each consecutive day.\n')

# get max days
maxDays = int(input('Input the total number of days worked: '))

# validate max days
dayCount = 1
pennies = 1

# accumulator (not needed)
#total_pay = 0

print('Day\tPennies Earned')
print('---\t--------------')
while dayCount <= maxDays:
    print(dayCount, '\t', pennies)
#   total_pay += pennies
    dayCount += 1
    pennies *=2

#print('\nTotal in dollar amount: $' ,format(total_pay, ',.2f'), sep = '')
print('\nTotal in dollar amount: $', format(pennies * 0.01, ',.2f'), sep = '')
input('\nPress Enter to exit.')
