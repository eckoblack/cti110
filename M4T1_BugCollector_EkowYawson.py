# A program to calculate running total of bugs collected for 5 days
# 19 June 2017
# CTI-110 M4T1 - Bug Collector
# Ekow Yawson
#



max = 5 #Number of Days

#initialize an accumulator variables.
total = 0.0
day = 0

#print welcome statement
print("This program calculates the sum of bugs collected for")
print(max, "days. \n")

#define for statement and print input and output
for day in range(max):
    number = int(input("Enter the total number of bugs collected today: "))
    total = total + number
    #day = day + 1
    print("The running total of bugs collected for day", day + 1)
    print('is', total, "\n")

#print final output
print("The overall total number of bugs collected for the 5 days is:", total)
input("Press enter to continue ")
