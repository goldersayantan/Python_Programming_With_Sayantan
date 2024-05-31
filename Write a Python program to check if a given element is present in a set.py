# Write a Python program to check if a given element is present in a set...
my_set = set()
limit = int(input("Enter the number of elements you want to add in set: "))
for i in range(limit):
    element = input(f"Enter the element number {i + 1}: ")
    my_set.add(element)
print("The set will be: ", my_set)

element = input("Enter the element to check in the set: ")
if element in my_set:
    print(f"{element} found in the set.")
else:
    print(f"{element} does not found in the set")
