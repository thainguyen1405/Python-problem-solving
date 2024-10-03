#Thai Nguyen, countercchar

#Ask for input
word = input()

#Set the loop to indicates how many times the character appears
count = 0
for i in range(1,len(word),1):
    if word[0] == word[i]:
        count = count+1
        i = i+1

#If statement to check how the appearance is 1 or not
if count == 1:
    print(str(count) + " " + str(word[0]))
elif count != 1:
    print(str(count) + " " + str(word[0])+ "'s")
    


