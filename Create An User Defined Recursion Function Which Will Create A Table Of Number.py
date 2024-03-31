# Create An User Defined Recursion Function Which Will Create A Table Of Number...
def table(x, product=1):
    if product <= 10:
        print(x, "*", product, "=", x * product)
        table(x, product + 1)


num = int(input("Enter a number to find its table: "))
print("The table is: ")
table(num)
