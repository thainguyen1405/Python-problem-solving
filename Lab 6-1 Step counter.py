#Define a function named feet_to_steps
def feet_to_steps(user_feet):
    steps = user_feet/2.5
    return steps

#Main program 
user_feet = float(input("Enter the feet walked: "))
steps = feet_to_steps(user_feet)
print(round(steps))
