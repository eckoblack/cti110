# A program that displays the total calories burned on a treadmill
# 19 June 2017
# CTI-110 M4HW1 - Calories Burned
# Ekow Yawson
#



#initialize an accumulator variables.
total = 0.0
burned = 4.2

#define input for minutes, and output of calories burned for x minutes
#minutes = int(input('Enter number of minutes ran on treadmill: '))
minutes = 30
for x in range (10, (minutes + 1), 5):
    cal_burned = burned * x
    print("You burned", cal_burned, "calories in", x, "minutes.")
    
