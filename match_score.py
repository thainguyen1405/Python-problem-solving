#Defined function named match_score
def math_score(first,second):
    #Check if the two string have the same length
    if len(first) != len(second):
        print("Match score: 0")

    elif len(first) == len(second):
       #Transfer the first string to the letter list
        list1 = []
        count = 0 
        for letter in first:
            list1.append(letter)

        #Check every letter of second string has in the first list
        h = 0
        for h in range(0,len(second),1):
            if second[h] in list1:
                count = count + 1
                h = h+1

        print("Match score: " + str(count))


#Ask for input
print("Enter the first string:", end=" ")
first = input()
print("Enter the second string:", end=" ")
second = input()
#Recall the function
math_score(first,second)
            
            
    
