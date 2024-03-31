# Create An User Defined Function With List As A Parameter And Make The Sum Of Alternate Elements...
def sum_alternate_elements(x):
    total = 0
    for i in range(0, len(x)):
        if i % 2 != 0:
            total = total + x[i]
    return total


lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("The sum of alternate elements in list will be: ", sum_alternate_elements(lst))
