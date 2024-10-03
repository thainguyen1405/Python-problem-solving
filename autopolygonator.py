
print("Enter the number sides of the polygon: ", end="")
n = int(input())
print("Enter the total length of the polygon: ", end="")
l = int(input())

import turtle
t = turtle.Turtle()

#Set the pen position
t.penup()
t.goto(-45,0)
t.pendown()


#The equation of the sum of interior angles: (n-2)*180
#a is the inside of each angle
#180-a is the outside of each angle

a = ((n-2)*180)/n
for i in range(n):
    t.forward(100)
    t.left(180-a)

