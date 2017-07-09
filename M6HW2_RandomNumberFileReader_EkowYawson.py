# This program reads a file created using a random number file generator program,
# gets the sum of and the amount of random numbers
# 7 July 2017
# CTI-110 M6HW2 - Random Number File Reader
# Ekow Yawson
#

def getRand():
#define getRand() function
    #opens and reads file 'randomNumbers.txt' and displays its contents
    readFile = open('randomNumbers.txt', 'r')
    displayFile = print(readFile.read())
    return displayFile


def main():
#define the main program
    print('This program will open a file named "randomNumbers.txt" and read\n\
its contents. It will then display its total and the amount of\n\
random numbers read.')
    print()
    print('Random Numbers')
    print('From Text File')
    print('--------------\n')
    #call getRand() function to display values (random numbers) in file
    getRand()
    print('--------------')
    #opens and reads file 'randomNumbers.txt' and displays its contents
    readFile = open('randomNumbers.txt', 'r')
    total = 0
    amount = 0
    #calculate total and amount
    for num in readFile:
        total += int(num)
        amount += 1
    #close file
    readFile.close()
    
    print("The total of all the numbers in the 'randomNumbers.txt' file is:", total)
    print('The number of random numbers read from the file is:', amount)

    #call main
main()
