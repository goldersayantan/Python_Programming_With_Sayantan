# Check A Year Is Leap Year Or Not...
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, "Is Leapyear")
    else:
        print(year, "Is Not leapyear")


x = int(input("Enter a year:"))
leap_year(x)
