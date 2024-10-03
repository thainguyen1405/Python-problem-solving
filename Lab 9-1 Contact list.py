# Ask for input also spliting the blank 
x = input("Enter the contact: ").split(sep=" ")

#Split the list by seperate the comma and get the name list
y = [item.split(",",1)[0] for item in x]

#Split the list seperate by the comma and get the phone number list
z = [item.split(",",1)[1] for item in x]

#Ask for the name
name = input("Enter the name: ")

#Checking if the name correspond the y list
for i in range(len(y)):
    if y[i] == name:
        print(z[i])
        break
