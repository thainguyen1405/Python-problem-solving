#Define the swap_values function
def swap_values(user_val1, user_val2, user_val3, user_val4):
    x = [user_val1,user_val2, user_val3, user_val4]

    #Swap the 1st with 2nd value
    a = x.index(user_val1)
    b = x.index(user_val2)
    x[b], x[a] = x[a], x[b]
    
    #Swap the 3rd with 4th value
    c = x.index(user_val3)
    d = x.index(user_val4)
    x[c], x[d] = x[d], x[c]

    print(x[a],x[b],x[c],x[d])


#Main program 
user_val1 = int(input("Enter the val1: "))
user_val2 = int(input("Enter the val2: "))
user_val3 = int(input("Enter the val3: "))
user_val4 = int(input("Enter the val4: "))

swap_values(user_val1, user_val2, user_val3, user_val4)
