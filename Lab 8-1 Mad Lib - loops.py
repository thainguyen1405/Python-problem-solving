#Make the while loop to get the condition
while True:
    name = input()
    #I split the input into list to indetify the name
    sepa = name.split()
    #Check if it is 'quit' to make a break
    if sepa[0] == 'quit':
        break
    print("Eating " + sepa[1] + " " + sepa[0] + " a day keeps you happy and healthy.")
