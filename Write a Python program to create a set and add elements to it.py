# Write a Python program to create a set and add elements to it...
my_set = set()
limit = int(input("Enter the number of elements you want to add in set: "))
for i in range(limit):
    element = int(input(f"Enter the element number {i + 1}: "))
    my_set.add(element)
print("The set will be: ", my_set)
