#Thai Nguyenn, Assignment 8.1
from graphics import *
import random

win = GraphWin("Graphics Test", 600, 600)


# Set size 
shape_size = 50

# Draw shapes in rectangle 
for row in range(10):
    for col in range(10):
        if (row + col) % 2 == 0:
            shape = Rectangle(Point(col*shape_size, row*shape_size), Point(col*shape_size + shape_size, row*shape_size + shape_size))
            shape.setFill('grey')
            shape.draw(win)
        else:
            shape = Rectangle(Point(col*shape_size, row*shape_size), Point(col*shape_size + shape_size, row*shape_size + shape_size))
            shape.setFill('pink')
            shape.draw(win)

# Add a diagonal line of circles
for i in range(10):
    shape = Circle(Point(i*shape_size + shape_size/2, i*shape_size + shape_size/2), shape_size/2)
    shape.setFill("brown")
    shape.draw(win)

# Add text to the window
text = Text(Point(win.getWidth()/2, win.getHeight() - 20), "Hi, I'm here!")
text.draw(win)
