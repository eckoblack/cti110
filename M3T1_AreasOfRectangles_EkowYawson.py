#Evaluate the area of two triangles and output the one with the greatest area
#12 June 2017
#CTI-110 M3T1 - Areas of Rectangles
#Ekow Yawson

#Define area of rectangle A
print("This program gets the length and width of two rectangles ((A) & (B)), calculates the area of both (A) & (B),\
and outputs which one has the greater area.\n")

length_A = float(input("Input the length of rectangle (A) (format: xx or xx.xx): "))
width_A = float(input("Input the width of rectangle (A) (format: xx or xx.xx): "))
area_A = length_A * width_A
print("The area of rectangle (A) is ", area_A)

#Define area of rectangle B
length_B = float(input("Input the length of rectangle (B) (format: xx or xx.xx): "))
width_B = float(input("Input the width of rectangle (B) (format: xx or xx.xx): "))
area_B = length_B * width_B
print("The area of rectangle (B) is ", area_B, ".\n")

#Set argument to return which area value is larger
if area_A > area_B:
    print("The area of rectangle (A) is larger.")
elif area_A < area_B:
    print("The area of rectangle (B) is larger.")
else:
    print("The area of the two rectangles are equal.")
input("Press enter to exit.")
