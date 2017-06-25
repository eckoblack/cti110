# A program that calculates Body Mass Index
# 15 June 2017
# CTI-110 M3HW2 - Body Mass Index
# Ekow Yawson
#


print('This program will calculate a person\'s Body Mass Index.\n\
A calculation used to tell if a person is underweight, overweight, or optimal weight. \n')
#Define terms
weight = float(input('Enter weight in pounds: '))
height = float(input('Enter height in inches: '))
BMI = weight * (703/height**2)

#Define main()
def main():
    if BMI < 18.5:
        print('This person is considered underweight')
    elif BMI >= 18.5 and BMI <= 25:
        print('This person\'s weight is optimal')
    else:
        print('This person is considered overweight')
    print('Your body mass index score is: ')
    print(format(BMI,".2f"))

    
#Output
main()


