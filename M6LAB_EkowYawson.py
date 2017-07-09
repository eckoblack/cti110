# A program that reads numbers stored in a file and calculates its sum
# 6 July 2017
# CTI-110 M6LAB - Sum Of Numbers
# Ekow Yawson
#



def main():
    #read numbers in a file 'numbers.txt' and calculate the sum of numbers
    print('This program will open a file named "numbers.txt" and display its contents.')
    print("It will then calculate a running total up to the final total.")
    print()
    readFile = open('numbers.txt', 'r')
    total = 0
    for num in readFile:
        total = total + int(num)
        print(total)
    readFile.close()
    print()
    print("The total of numbers in the file 'numbers.txt' is:", total)

main()
