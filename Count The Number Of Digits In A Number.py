# Count The Number Of Digits In A Number...
num = int(input("Enter a number: "))
temp = num
count = 0
while temp > 0:     # Condition
    temp = temp//10
    count += 1      # Increasing The Value Of 'i' with 1
print("The number of digits in", num, "is: ", count)
