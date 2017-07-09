# A program that displays a series of integers in a text file
# 5 July 2017
# CTI-110 M6T1 - File Display
# Ekow Yawson
#


#open file numbers.txt
def main():
    print('This program will open a file named "numbers.txt" and display its contents.')
    print()
    readFile = open('numbers.txt', 'r')
    fileContents = readFile.read()
#close file
    readFile.close()
#display numbers in file
    print(fileContents)

#call main
main()
