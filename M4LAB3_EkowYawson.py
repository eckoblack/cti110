# Import turtle program and use to draw snowflake
# 20 June 2017
# CTI-110 M4LAB3: Snowflake
# Ekow Yawson
#


import turtle

fun = turtle.Screen()
fun.bgcolor("black")
sides = 12

def main():
    ekow = turtle.Turtle()
    reta = turtle.Turtle()
    ekow.color("red")
    reta.color("blue")
    ekow.speed(10)
    reta.speed(10)


    for i in range(sides):
        create(ekow)
        create(reta)
        ekow.right(52)
        reta.right(88)

def create(t):
    for i in range(sides):
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.right(180)

main()
