#Calculate the distance that a car travels down an interstate
#8 June 2017
#CTI-110 M2HW1 - Distance Traveled
#Ekow Yawson


#Defining distance = speed * time
print("This program will calculate the distance traveled in miles\ngiven the speed and time.")
speed = int(input("Input the speed of the vehicle in miles per hour (ex: 75): "))
time = float(input("Input the time of travel in hours and decimal (ex: 7.5 for 7 hours and 30 mins): "))
distance = speed * time

#Output
print("The distance that the vehicle will travel in", time, " hours is", distance, "miles.")
