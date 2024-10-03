print("Enter the number of moviegoers:", end=" ")
moviegoers = int(input())
if moviegoers <= 25:
    print("The total ticket price is $ " + str("${:.2f}".format((moviegoers-1)*12+9.50)) + ".")
if moviegoers > 25:
    print("The total ticket price is $ " + str("${:.2f}".format(moviegoers*7.25)) + ".")
    
