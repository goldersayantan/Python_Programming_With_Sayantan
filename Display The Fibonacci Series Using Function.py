# Display The Fibonacci Series Using Function...
def fibonacci(x):
    temp1 = 0
    temp2 = 1
    print("The fibonacci series will be: ")
    for i in range(0, x):
        print(temp1)
        backup = temp2
        temp2 = temp1 + temp2
        temp1 = backup


limit = int(input("Enter the number of numbers you want to display in fibonacci series: "))
fibonacci(limit)



# Display the fibonacci series using function...
def fibonacci(x):
    temp1 = 0
    temp2 = 1
    while temp1 < x:
        print(temp1)
        temp1, temp2 = temp2, temp1 + temp2


limit = int(input("Enter the limit: "))
print("The fibonacci series will be: ")
fibonacci(limit)
