# Given a tuple of integers, write a Python program to find the largest and smallest elements.
temp_lst = []
limit = int(input("Enter the number of elements you want to add in tuple: "))
for i in range(limit):
    element = int(input(f"Enter the element number {i + 1}: "))
    temp_lst.append(element)
my_tup = tuple(temp_lst)
print("The largest element is: ", max(my_tup))
print("The smallest element is: ", min(my_tup))
