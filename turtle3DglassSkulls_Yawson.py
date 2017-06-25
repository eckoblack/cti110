#Ekow
#Turtle Practice 2
#20 June 2017


import turtle
import math

def main():
    win = turtle.Screen()
    win.bgcolor("black")

    gyan = turtle.Turtle()
    ekow = turtle.Turtle()
    gyan.pencolor("red")
    ekow.pencolor("blue")
    gyan.speed(10)
    ekow.speed(10)


    for i in range(sides + sides):
        gTurn(gyan)
        eTurn(ekow)
        gTurn(ekow)
        eTurn(gyan)
        sgTurn(ekow)
        seTurn(gyan)
        seTurn(ekow)
        sgTurn(gyan)
        
        
       
a = 50
b = 50
c = math.sqrt(a**2 + b**2)
sides = 10
angle = 360/(sides)
        
def gTurn(t):
    for i in range(12):
        t.right(angle + 45)
        t.forward(b)

def eTurn(t):
    for i in range(12):
        t.right(angle)
        t.forward(a)

def sgTurn(t):
    for i in range(12):
        t.right(angle + 45)
        t.forward(c)

def seTurn(t):
    for i in range(12):
        t.right(angle)
        t.forward(c)
        
    
main()
