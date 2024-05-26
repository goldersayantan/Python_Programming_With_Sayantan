# Check a number is prime or composite...
num = int(input("Enter a number to check if it is a prime number: "))
prime = 0
for i in range(2, num):
    if num % i == 0:
        prime = 0
        break
    else:
        prime = 1

if num == 0:
    print("0 is not considered as a prime or composite number")
elif num == 1:
    print(f"{num} is neither prime nor a composite number")
elif num == 2:
    print(f"{num} is a prime number")
elif num < 0:
    print("Negative numbers are not considered as prime or composite numbers")
elif prime == 0:
    print(f"{num} is a composite number")
else:
    print(f"{num} is a prime number")
