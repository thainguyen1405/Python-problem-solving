import random
x = random.randrange(1,256)
test_str = """ "odd" or "even". """
print("I'm thinking of a number. Is it odd or even?", end=" ")
y = input()
if (x%2) == 0:
   if str(y) == "even":
      print("My number was " + str(x) + ". Well done!")
   elif str(y) == "odd":
      print("My number was " + str(x) + ". Sorry!")

if (x%2) != 0:
   if str(y) == "odd":
      print("My number was " + str(x) + ". Well done!")
   elif str(y) == "even":
      print("My number was " + str(x) + ". Sorry!")

if str(y) != "odd" and str(y) != "even":
   print("You didn't enter" + test_str +"You forfeit!" + " (My number was " + str(x) + " if you're wondering.)")






