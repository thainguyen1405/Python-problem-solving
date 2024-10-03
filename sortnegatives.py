#Thai Nguyen, sortnegatives

#Ask for input
num = input("Enter the list of integers: ")
#split the input into list
list1 = num.split()

#Create a new list by collecting negative number
list2 = []
for i in range(len(list1)):
    if int(list1[i])<0:
        list2.append(int(list1[i]))

#Sort the list in desceding order
list2.sort(reverse=True)

#Print the list without the bracket
for m in range(len(list2)):
    print(list2[m], end =" ")
