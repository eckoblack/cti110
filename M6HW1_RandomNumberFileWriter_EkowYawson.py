# A program that writes a series of random numbers to a file
# 5 July 2017
# CTI-110 M6HW1 - Random Number File Writer
# Ekow Yawson
#


import random

def getNum():
    #get the amount of random numbers
    howMany = int(input('How many random numbers would you like to write\
 to a file? '))
    return howMany

def genRand():
    #print the random numbers and save to file function
    amount = getNum()
    randNum = random.randint(1,500)
    for num in range(amount):
        randNum = random.randint(1,500)
    #create file
        createFile = open('randomNumbers.txt', 'a')
        createFile.write(str(randNum) + '\n')
        createFile.close()
        print(randNum)
    print('Your numbers have been written to a file named randomNumbers.txt.')
    return randNum
    
def main():
    #greeting and main program
    print("This program will print out a user defined amount of 'random numbers'.")
    print()
    genRand()
    
main()
