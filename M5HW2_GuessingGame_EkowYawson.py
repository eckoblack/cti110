# A program that generates a random number in range 1-100 and asks user to guess
# 28 June 2017
# CTI-110 M5HW2 - Random Number Guessing Game
# Ekow Yawson
#


import random

#greeting
print('\n\t\tThis is a random number geussing game.\n')
print('The program will generate a random number from 1 to 100 and ask you\
\nto guess the number.\n')
print('You will have an unlimited number of guesses, however, an optimal guess\
\nwould be in six or less attempts.\n')

#generate random number
randNum = random.randint(1,100)

#define main
def main():
    number=int(input('Enter a number between 1 and 100 (including 1 and 100): '))
    guess(number)

#get guess
def guess(number):
    randNum = random.randint(1,100)
    guesses = 0
    while randNum < 101:
        
        #get number of guesses taken
        guesses += 1
        print('Try number', guesses)
        if number == randNum:
            numGuesses = guesses
                    
        #actions if number is guessed in six or less tries
            if numGuesses <= 6:
                print('\nAMAZING!!! YOU GUESSED THE NUMBER IN', numGuesses, 'TRIES!!!')
                print('AWESOME!!!')
                print('The number is ', randNum,'.', sep='')
                runAgain = input('Play again? (y or n): ')
                if runAgain == 'y' or runAgain == 'Y':
                    print()
                    main()
                else:
                    break
                
        #actions if number is guessed in more than 6 tries
            print('\nHooray you guessed the number!! Congratulations!')
            print('The number is', randNum)
            print('You guessed the number in', numGuesses, 'tries!')
            runAgain = input('Play again? (y or n): ')
            if runAgain == 'y' or runAgain == 'Y':
                print()
                main()
            else:
                break
            
        #actions if wrong number is guessed
        elif number > randNum:
            print('Too high, try again.\n')
            number=int(input('Enter a number between 1 and 100 (including 1 and 100): '))
        else:
            print('Too low, try again.\n')
            number=int(input('Enter a number between 1 and 100 (including 1 and 100): '))

#run main
main()
