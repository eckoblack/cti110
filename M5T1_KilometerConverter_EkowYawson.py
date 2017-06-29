# A program that converts kilometers to miles
# 26 June 2017
# CTI-110 M5T1_KilometerConverter 
# Ekow Yawson
#


# This program asks the user to enter a distance in kilometers, and then converts
# it to miles.
# Miles = Kilometers * 0.6214

#def the main function
def main():
    print('This program converts a kilometer distance value to miles.\n')   #greeting
    
#def conversion values
    def milesTokilos():
        kilo_value = float(input('Please input the distance in kilometers to be converted: ')) #get kilo value
        print()
        miles_value = kilo_value * 0.6214
        print(kilo_value, 'kilometers converts to', format(miles_value, ',.2f'), 'miles.')
        print()
#run milesTokilos
    milesTokilos()

#ask user whether to run again
    def run_again():
        runAgain = input('Would you like to convert another value? (y or n): ')
        print()
        while runAgain == 'y' or runAgain == 'Y':
            milesTokilos()
            runAgain = input('Would you like to convert another value? (y or n): ')
            print()

#run run_again
    run_again()

#call main function    
main()
