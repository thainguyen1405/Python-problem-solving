#s is the slope, i is the intercept
print("Enter the slope:", end=" ")
s = float(input())
print("Enter the intercept:", end=" ")
i = float(input())
print("Line y = " + str(s) + " x + " + str(i) + " :")

#a plays as value of x, y plays as value of y from (0,1,2,...,9)
a = 0
y = s*a + i
while a<10:
    print("At x = " + str(a), ", y = " + str(y))
    a = a+1
    y = s*a + i

#b plays as value of x, z plays as value of y from (10,100,...,100,000)
b = 10
z = s*b + i
while b<= 100000:
    print("At x = " + str(b), ", y= " + str(z))
    b = b*10
    z = s*b + i

