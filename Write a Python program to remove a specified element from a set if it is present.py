# Write a Python program to remove a specified element from a set if it is present...
my_set = set()
limit = int(input("Enter the number of elements you want to add in set: "))
for i in range(limit):
    element = input(f"Enter the element number {i + 1}: ")
    my_set.add(element)
print("The set will be: ", my_set)
remove_element = input("Enter the element you want to delete from the set: ")
if remove_element in my_set:
    my_set.remove(remove_element)
    print("Element removed successfully.")
    print("Now the new set will be: ", my_set)
else:
    print("Element not found")
