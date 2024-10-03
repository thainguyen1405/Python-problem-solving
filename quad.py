import math

#Define the determinant 
def determinant(a,b,c):
    d = float((b**2)-(4*a*c))
    if d>0:
        print("The quadratic has two roots: " + str(first_root(a,b,c)) + " and " + str(second_root(a,b,c)))
    if d==0:
        print("That quadratic has one root: " + str(first_root(a,b,c)))
    if d<0:
        print("Sorry, that quadratic has complex roots.")


#Define and return the 1st root        
def first_root(a,b,c):
        d = float((b**2)-(4*a*c))
        x = float((-b+math.sqrt(d))/(2*a))
        return x


#Define and return the 2nd root
def second_root(a,b,c):
        d = float((b**2)-(4*a*c))
        y = float((-b-math.sqrt(d))/(2*a))
        return y


#Main program 
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

determinant(a,b,c)

