# Check A Number Is Prime Or Composite...
def prime_composite(x):
    temp = 0
    for i in range(x, 1):
        if x % i == 0:
            temp = 1
        else:
            temp = 2

    if temp == 1:
        print(x, "is a composite number")
    elif temp == 0:
        print(x, "is neither prime nor composite")
    elif temp == 2:
        print(x, "is a prime number")
    else:
        print("invalid number")


num = int(input("Enter a number: "))
prime_composite(num)
