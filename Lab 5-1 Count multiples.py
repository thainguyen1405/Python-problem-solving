low = int(input())
high = int(input())
x = int(input())
i = low
count = 0
for i in range(low,high+1,1):
    if i % x == 0:
        count = count+1
print(count)

    
       
