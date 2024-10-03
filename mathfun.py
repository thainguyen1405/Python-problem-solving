import math

#a is opposite
#b is adjacent 
#c is hypotenuse
#θ is adjacent angle 


#Calculate adjacent length given hypotenuse and the adj angle
def adjacent_length(a,b,c,θ):
    b = math.cos(math.radians(θ))*c
    return b

#Calculate opposite length given hypo and the adj angle
def opposite_length(a,b,c,θ):
    a = math.sin(math.radians(θ))*c
    return a

#Calculate adj angle given hypo and oppo lengths
def adjacent1_angle(a,b,c):
    angle1 = math.degrees(math.asin(a/c))
    return angle1

#Calculate adj angle given adj and oppo lengths
def adjacent2_angle(a,b,c):
    angle2 = math.degrees(math.atan(a/b))
    return angle2


#Main program
a = float(input("Enter the oposite length: "))
b = float(input("Enter the adjacent length: "))
c = float(input("Enter the hypotenuse length: "))
θ = float(input("Enter the adjacent angle: "))

print("Adjacent length: " + str(adjacent_length(a,b,c,θ)))
print("Opposite length: " + str(opposite_length(a,b,c,θ)))
print("Adjacent angle: " + str(adjacent1_angle(a,b,c)))
print("Adjacent angle: " + str(adjacent2_angle(a,b,c)))
