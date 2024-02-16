# Calculating Permutation And Combination...
def factorial(n1):
    fact = 1
    for i in range(n1, 0, -1):
        fact = fact * i
    return fact                 # Calculating The Factorial...


def permutation(n2, r2):
    return factorial(n2) // factorial(n2 - r2)                  # Calculating The Value Of Permutation...


def combination(n3, r3):
    return factorial(n3) // (factorial(r3) * factorial(n3 - r3))    # Calculating The Value Of Combination...


n = int(input("Enter the amount of n: "))
r = int(input("Enter the amount of r: "))
print("The permutation value is: ", permutation(n, r))
print("The combination value is: ", combination(n, r))
