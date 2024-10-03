#Define fibonacci function
def fibonacci(n):
    i = [0,1]
    x = 1
    for x in range(0,n+1,1):
        i.insert(x+1, i[x] + i[x-1])

    return i[n]

#Main program
n = int(input("Enter the n index: "))
if n<0:
    print("fibonacci(" + str(n) + ") is " + str(-1))
elif n>0:
    print("fibonacci(" + str(n) + ") is " + str(fibonacci(n)))

