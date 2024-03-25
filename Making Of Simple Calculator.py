# Making Of Simple Calculator.....
# Write a Python program to perform the basic four operators(+, -, *, /).....
num1 = input("Enter the first number: ")
if num1.isdigit():
    num2 = input("Enter the second number: ")
    if num2.isdigit():
        operator = input("Enter the operator: ")
        if operator == "+":
            print("The sum will be: ", int(num1) + int(num2))
        elif operator == "-":
            print("The difference will be: ", int(num1) - int(num2))
        elif operator == "*":
            print("The multiplication will be: ", int(num1) * int(num2))
        elif operator == "/":
            print("The division will be: ", int(num1) / int(num2))
        elif operator == "//":
            print("The float division will be: ", int(num1) // int(num2))
        elif operator == "%":
            print("The remainder will be: ", int(num1) % int(num2))
        else:
            print("Invalid operator")
    else:
        print("Invalid input")
else:
    print("Invalid input")
