# This program calculates the average of all numbers stored in a file
# and handles IOError and ValueError exceptions.
# 9 July 2017
# CTI-110 M6HW3 - Exception Handling
# Ekow Yawson
#

def getNumbers(file):
#opens, reads and prints values from specified file.
    readFile = open(file, 'r')
    displayFile = readFile.read()
    print(displayFile)
    return displayFile

def avg(file):
#gets the average of numbers in specified file.
    readFile = open(file, 'r')
    total = 0
    amount = 0
    #get total and amount of numbers
    for num in readFile:
        total += int(num)
        amount += 1
    #get average
    avg = total/amount
    print("The average of all numbers in the file '", file, "' is:", format(avg, ',.2f'))
    readFile.close()
    return avg

def main():
#define the main program
    print()
    print('This program will open a text file and read its numerical\n\
contents. It will then calculate the average of the numbers.\n')
    #define file = filename
    file = 'numbers.txt'
    print('Numbers From Text File')
    print('----------------------')
    
    try:
        #call getNumbers() and avg() functions, and handle exceptions
        getNumbers(file)
        print('----------------------')
        avg(file)
        
    except ValueError:
        print('Error: All values in the file must be valid numbers.\n')
        
    except IOError:
        print('Error: An error occurred while attempting to locate and read\
 the file.\n')
        
    except:
        print('An error occured.')
    
    #call main
main()
