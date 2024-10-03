def days_in_feb(user_year):
    if user_year % 100 == 0:
        if user_year/100 % 4 == 0:
            return x
        elif user_year/100 % 4 != 0:
            return x-1
    if user_year % 4 == 0:
        return x
    elif user_year % 4 != 0:
        return x-1

x=29
user_year = int(input("Enter the year you want: "))
x = days_in_feb(user_year)
print(str(user_year) + " has " + str(x) + " days in February.")
