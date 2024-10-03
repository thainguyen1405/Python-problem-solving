#Thai Nguyen, list_methods

#Ask and split the input 
num = input()
Snum = num.split()

#Add the input into the list
list1 = []
for i in range(len(Snum)):
    list1.append(int(Snum[i]))

#1. Print the sum
print(sum(list1))

#2. Print the max and min
print(max(list1))
print(min(list1))

#3. Sort the list in ascending order(not remove duplicate yet)
list1.sort()
print(list1)


#Deine the function
def duplicate(list1):
    #Add any int from list1 to newlist by checking there's no duplicate
    newlist = []
    for m in list1:
        if m not in newlist:
            newlist.append(m)

    return newlist

#4. Remove all the duplicates 
print(duplicate(list1))
