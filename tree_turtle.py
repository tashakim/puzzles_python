import numpy as np
import turtle
import random

def tree(branchLen,t):
    """
    Purpose: Recursively draws random tree 
    """
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-random.randint(10,20),t)
        t.left(40)
        tree(branchLen-random.randint(10,20),t)
        t.right(20)
        t.backward(branchLen)


def draw_init(turtle, color):
    """
    Purpose: Initializes turtle position and color
    """
    print("Turtle initialized")

    turtle.left(90)
    turtle.up()
    turtle.backward(100)
    turtle.down()

    turtle.color(color)
    tree(75,turtle)
    print("Turtle finished drawing tree")
    

def main():
    myWin = turtle.Screen()
    color = ['red', 'yellow', 'green', 'blue']

    for i in range(4):
        t = turtle.Turtle()
        draw_init(t, color[i%3])
    myWin.exitonclick()

if __name__ == '__main__':
    main()
