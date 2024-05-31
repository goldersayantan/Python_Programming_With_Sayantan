# Given a list of integers, write a Python program to find the second-largest element.
my_lst = []
limit = int(input("Enter the number of elements you want to add in the list: "))
for i in range(limit):
    element = int(input(f"Enter the element number {i + 1}: "))
    my_lst.append(element)
print("The given list is: ", my_lst)
largest_element = max(my_lst)       # largest element...
temp_lst = my_lst.copy()            # Copying the given list...
temp_lst.remove(largest_element)    # Removing the largest element...
print("The second-largest element from the given list is: ", max(temp_lst))
