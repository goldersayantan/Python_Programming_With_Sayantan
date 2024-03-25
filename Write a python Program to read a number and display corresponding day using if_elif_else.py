# Write a python Program to read a number and display corresponding day using if_elif_else.....
day_num = int(input("Enter the number according to date(1 - 7): "))
if day_num == 1:
    print("The day is Monday.")
elif day_num == 2:
    print("The day is Tuesday.")
elif day_num == 3:
    print("The day is Wednesday.")
elif day_num == 4:
    print("The day is Thursday")
elif day_num == 5:
    print("The day is Friday")
elif day_num == 6:
    print("The day is Saturday")
elif day_num == 7:
    print("The day is Sunday")
else:
    print("invalid number")
