# Sum Of First N Natural Number Using Recursion...
def sum_natural_numbers(x):
    if x == 1:
        return 1
    else:
        return x + sum_natural_numbers(x-1)


num = int(input("Enter the starting number: "))
print("The sum of natural numbers is: ", sum_natural_numbers(num))
