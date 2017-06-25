# Import turtle program and use to draw snowflake
# 20 June 2017
# CTI-110 M4LAB3: Snowflake
# Ekow Yawson
#

import random
import turtle

fun = turtle.Screen()
fun.bgcolor("black")
sides = 12


def main():
    ekow = turtle.Turtle()
    reta = turtle.Turtle()
    ekow.color("silver")
    reta.color("cyan")
    ekow.speed(10)
    reta.speed(10)
    ekow.penup()
    reta.penup()
    ekow.setpos(0, 100)
    reta.setpos(0, 100)
    ekow.pendown()
    reta.pendown()


    for i in range(sides):
        create(ekow)
        create(reta)
        ekow.right(42)
        reta.right(78)

    def flake(size, ekow):
        ekow.pensize(size / 10)

        if size < random.randint(1,2) * 20:
            ekow.color("cyan")

        if size > 5:
            ekow.forward(size)
            ekow.right(55)
            flake(size - random.randint(10, 20), ekow)
            ekow.left(110)
            flake(size - random.randint(10, 20), ekow)
            ekow.right(55)
            ekow.penup()
            ekow.backward(size)
            ekow.pendown()

    flake(120, ekow)

def create(t):
    for i in range(2):
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(120)



main()
