# Table Of Numbers In A Specific Range...
print("Here you can print the tables of numbers in a specific range: ")
num1 = int(input("Enter the beginning number: "))
num2 = int(input("Enter the ending number: "))

for i in range(num1, num2+1):
    for j in range(1, 11):
        print(i, "*", j, "=", i*j)
    print("---------------")
