import turtle
my_screen = turtle.getscreen()
v = turtle.Turtle()

my_screen.bgcolor("#DBDBD6")
v.pencolor("black")

#Draw and fill the 1st tire
v.begin_fill()
v.forward(150)
v.fillcolor("yellow")
v.right(90)
v.circle(30,180)
v.right(90)
v.end_fill()
v.forward(70)

#Draw and fill the body
v.begin_fill()
v.fillcolor("#6EFAD6")
v.left(90)
v.forward(150)
v.left(90)
v.forward(500)
v.left(90)
v.forward(150)
v.left(90)
v.forward(50)
v.end_fill()

#Draw and fill the 2nd tire
v.begin_fill()
v.fillcolor("yellow")
v.right(90)
v.circle(30,180)
v.right(90)
v.end_fill()
v.forward(350)
v.backward(430)

#Draw a window
v.penup()
v.goto(170,70)
v.pendown()
v.begin_fill()
v.forward(50)
v.fillcolor("#FBB875")
v.left(90)
v.forward(50)
v.left(90)
v.forward(50)
v.left(90)
v.forward(50)
v.end_fill()

#Draw a door
v.penup()
v.goto(80,0)
v.pendown()
v.begin_fill()
v.fillcolor("#F4819E")
v.left(90)
v.forward(30)
v.left(90)
v.forward(80)
v.left(90)
v.forward(50)
v.left(90)
v.forward(80)
v.end_fill()


#Draw a logo 
v.penup()
v.goto(-160,45)
v.pendown()
v.begin_fill()
v.fillcolor("white")
v.left(90)
v.forward(40)
v.left(90)
v.forward(60)
v.right(90)
v.forward(40)
v.left(45)
v.end_fill()

