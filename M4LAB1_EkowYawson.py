# Import turtle program and use to draw shapes
# 20 June 2017
# CTI-110 M4LAB1: Shapes
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

#draw shapes
e.left(180)

for i in range(4):
    e.right(120)
    e.forward(150)
    e.right(120)
    for i in range(1,5):
        e.forward(150)
        e.left(90)

e.pencolor("blue")

for i in range(4):
    e.right(120)
    e.forward(250)
    e.right(120)
    for i in range(1,5):
        e.forward(250)
        e.left(90)


win.mainloop()
