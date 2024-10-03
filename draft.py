from graphics import *
import random

win = GraphWin("Graphics Test", 600, 600)

# Set number of rows and columns
rows = 10
cols = 10

# Set size and color of shapes
shape_size = 50
shape_color = color_rgb(255, 0, 0)

# Draw shapes in a grid
for row in range(rows):
    for col in range(cols):
        if (row + col) % 2 == 0:
            shape = Circle(Point(col*shape_size + shape_size/2, row*shape_size + shape_size/2), shape_size/2)
            shape.setFill(shape_color)
            shape.draw(win)
        else:
            shape = Rectangle(Point(col*shape_size, row*shape_size), Point(col*shape_size + shape_size, row*shape_size + shape_size))
            shape.setFill(shape_color)
            shape.draw(win)

# Add a diagonal line of circles
for i in range(cols):
    shape = Circle(Point(i*shape_size + shape_size/2, i*shape_size + shape_size/2), shape_size/2)
    shape.setFill("green")
    shape.draw(win)

# Add custom color and random locations for triangles
for i in range(3):
    x1 = random.randint(0, win.getWidth() - shape_size)
    y1 = random.randint(0, win.getHeight() - shape_size)
    x2 = x1 + shape_size
    y2 = y1 + shape_size
    x3 = x1 + shape_size/2
    y3 = y1
    color = color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    shape = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    shape.setFill(color)
    shape.draw(win)

# Add text to the window
text = Text(Point(win.getWidth()/2, win.getHeight() - 20), "Hello, world!")
text.draw(win)

# Animate shape when moused over
def animate_shape(shape):
    while True:
        shape.move(random.randint(-5, 5), random.randint(-5, 5))
        time.sleep(0.1)

# Change thickness and color of outline for shapes
for i in range(cols):
    shape = Line(Point(i*shape_size, 0), Point(i*shape_size, win.getHeight()))
    shape.setWidth(3)
    shape.setOutline("blue")
    shape.draw(win)
    
win.getMouse()
win.close()
