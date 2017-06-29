# A program that displays five test scores
# 28 June 2017
# CTI-110 M5HW1 - Test Average and Grade
# Ekow Yawson
#

#greeting
print('This program will get five test scores, display the letter grade for each,\
\nand the average of all five scores. \n')

#get five test scores
score1 = float(input('Enter test score 1: '))
score2 = float(input('Enter test score 2: '))
score3 = float(input('Enter test score 3: '))
score4 = float(input('Enter test score 4: '))
score5 = float(input('Enter test score 5: '))

#display a letter grade for each score
def determine_grade(score):
    if score >= 90:
        print('letter grade: A')
    elif score >= 80:
        print('letter grade: B')
    elif score >= 70:
        print('letter grade: C')
    elif score >= 60:
        print('letter grade: D')
    else:
        print('letter grade: E')
    return score

#display average test score
def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    print('The average is: ', average)
    return average

#define main
def main():
    print('-----------------------------------------------------------------------')
    print('Test score 1')
    determine_grade(score1)
    print('Test score 2')
    determine_grade(score2)
    print('Test score 3')
    determine_grade(score3)
    print('Test score 4')
    determine_grade(score4)
    print('Test score 5')
    determine_grade(score5)
    print('-----------------------------------------------------------------------')
    calc_average(score1, score2, score3, score4, score5)

#run main
main()
