import numpy as np
import turtle
import random

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-random.randint(10,20),t)
        t.left(40)
        tree(branchLen-random.randint(10,20),t)
        t.right(20)
        t.backward(branchLen)

def draw(turtle):
    # Purpose: Recursively draws random tree 
    print("Turtle initialized")

    turtle.left(90)
    turtle.up()
    turtle.backward(100)
    turtle.down()

    turtle.color('green')
    tree(75,turtle)
    

def main():

    myWin = turtle.Screen()

    for i in range(4):
        t = turtle.Turtle()
        draw(t)
    myWin.exitonclick()

main()
