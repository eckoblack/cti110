# Import turtle program and use to draw initials
# 20 June 2017
# CTI-110 M4LAB2: Initials
# Ekow Yawson
#



import turtle
win = turtle.Screen()
e = turtle.Turtle()

#display options
e.pensize(6)
e.pencolor("red")
e.shape("turtle")
e.speed(5)

#draw E
e.left(180)

for i in range(1,4):
    e.forward(100)
    e.left(90)

for i in range(1,4):
    e.left(90)
    e.forward(100)

for i in range(1,2):
    e.forward(70)
    e.left(90)

#draw M Y
e.forward(200)
e.right(155)
e.forward(200)
e.left(130)
e.forward(200)
e.right(155)
e.forward(200)
e.left(90)
e.forward(100)
e.left(90)
e.forward(125)
e.left(45)
e.forward(100)
e.backward(100)
e.left(90)
e.backward(100)


win.mainloop()
