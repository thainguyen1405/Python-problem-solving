#Making lists of service using dictionaries 
x = dict()
x['Base car wash'] = 10
x['Tire shine'] = 2
x['Wax'] = 3
x['Rain repellent'] = 2

#Ask for input
y = input("Enter the 1st service: ")
z = input("Enter the 2nd service: ")


print("ZyCar Wash")
print("Base car wash - $10")

#Check if the input is in the data
if y in x:
    print(str(y) + " - "  + "$" + str(x[y]))
else:
    x[y] = 0
      
if z in x:
    print(str(z) + " - "  + "$" + str(x[z]))
else:
    x[z] = 0

#Print the total price
print("-----")
print("Total price: " + "$" + str(10+ x[y] + x[z]))
