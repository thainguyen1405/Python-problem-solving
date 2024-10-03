x = int(input())
y = int(input())
z = int(input())

if x< min(y,z):
    print(x)
if y< min(x,z):
    print(y)
elif z< min(x,y):
    print(z)
