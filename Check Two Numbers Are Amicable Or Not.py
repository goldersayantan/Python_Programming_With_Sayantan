# Check Two Numbers Are Amicable Or Not...
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
total1 = 0
total2 = 0
for i in range(1, num1):
    if num1 % i == 0:
        total1 = total1 + i
for j in range(1, num2):
    if num2 % j == 0:
        total2 = total2 + j
if total1 == num2 and total2 == num1:
    print(num1, "and", num2, "Are Amicable Numbers")
else:
    print(num1, "and", num2, "Are Not Amicable Numbers")
