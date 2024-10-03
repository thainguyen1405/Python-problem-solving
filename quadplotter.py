#Thai Nguyen, quadplotter

#Define the quadratic function
def quadratic_function(a,b,c):
    f = float(a*(x**2 )+ b*x + c)
    return f


#Main program

#Asking for input 
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))


#The parabola y when x from 0 to 9
x = 0
print("Parabola y = " + str(a) + " x^2 + " + str(b) + " x + " + str(c))
while x < 10:
    print("At x = " + str(x) + ", y = " + str(quadratic_function(a,b,c)))
    x = x+1


#The parabola y when x from 10 to 10000000
x = 10
while x <= 10000000:
    print("At x = " + str(x) + ", y = " + str(quadratic_function(a,b,c)))
    x = x*10
