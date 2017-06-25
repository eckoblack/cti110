# A program that outputs age classification based on user input of age
# 15 June 2017
# CTI-110 M3HW1 - Age Classifier
# Ekow Yawson
#



print("This program will output an age classification based on an input of age.\n")

#Define age &
#Create conditions for output
def main():
    age = float(input("Enter a person's age. If less than 1, input age in decimal (ie: .5 equals 6 months): "))
    if age <= 1:
        print("This person is an infant.")
    elif age < 13:
        print("This person is a child.")
    elif age < 20:
        print("This person is a teenager.")
    else:
        print("This person is an adult.")

#Run main
main()

input("Press Enter to exit")
