# Swapping Of Two variables With Third Variable...
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

num3 = num1
num1 = num2
num2 = num3

print("After swapping:- ")
print("The first number is: ", num1)
print("The second number is: ", num2)

# Without Third Variable...
num3 = int(input("Enter the first number: "))
num4 = int(input("Enter the second number: "))


num3 = num3 + num4
num4 = num3 - num4
num3 = num3 - num4

print("After swapping:- ")
print("The first number is: ", num3)
print("The second number is: ", num4)
