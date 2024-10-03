#Thai Nguyen, nameformat
name = input()
blank = 0

#This loop created to check how many blank between words
for i in range(0,len(name),1):
    if name[i] == " ":
        blank = blank+1

#If blank = 1 means the input has firstName " " lastName
if blank == 1:
    for h in range(0,len(name),1):
        if name[h] == " ":
            break
        h = h+1
    #print the name from the start of the blank and the first initial
    print(name[h+1:len(name)] + ", " + name[0] + ".")


#If blank != 1 means the input has last, middle and first name 
elif blank != 1:
    #Find the first blank to identify the middle Initial 
    for m in range(0,len(name),1):
        if name[m] == " ":
            break
        m = m+1

    #Find the second blank to identify the last Initial 
    for n in range(m+1,len(name),1):
        if name[n] == " ":
            break
        n = n+1
    #print the name from the start of second blank and the two first and middle intial
    print(name[n+1:len(name)] + ", " + name[0] + "." + name[m+1] + ".")
    
