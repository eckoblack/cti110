# A program that converts feet to inches
# 26 June 2017
# CTI-110 M5T2_FeetToInches 
# Ekow Yawson
#





#define main
def main():
    print('This program will convert feet values you input into inches.')
    print()
    feetToinches()
    
def run_again():
    again = input('Would you like to convert another value?(y or n): ')
    if again == 'y' or again == 'Y':
        feetToinches()
        again = input('Would you like to convert another value?(y or n): ')

def feetToinches():
    feet = float(input('Enter value in feet to be converted: '))
    inches = feet * 12
    print()
    print(feet, 'feet = ',format(inches, ',.2f'), 'inches.')
    print()
    run_again()


main()
    
