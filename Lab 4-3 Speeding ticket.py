x = int(input())
y = int(input())
# x is the speed limit, y is the driving speed

if y-x <= -10:
    print(50)
if y-x <= 20 and y-x >= 6:
    print(75)
if y-x > 20 and y-x <= 40:
    print(150)
if y-x > 40:
    print(300)
elif y-x > -10 and y-x < 6:
    print(0)
