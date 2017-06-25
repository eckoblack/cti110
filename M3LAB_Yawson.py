# Debugging a pre-written code
# 13 June 2017
# CTI-110 M3LAB - Debugging
# Ekow Yawson
#


print("This program will output a letter grade based on an input of a raw (number) grade.\n")
#Define score
score = float(input('Input your raw score: \n'))


#Create conditions for inputs
if score >= 90:
    print("Your grade is A.")
elif score >= 80:
    print("Your grade is B.")
elif score >= 70:
    print("Your grade is C.")
elif score >= 60:
    print("Your grade is D.")
else:
    print("Your grade is F.")
    
