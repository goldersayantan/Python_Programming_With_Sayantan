# Write a Python program to create a tuple of tuples from a given list of integers...
my_lst = []
limit = int(input("Enter the number of elements you want in your list: "))
for i in range(limit):
    element = int(input(f"Enter the element number {i + 1}: "))
    my_lst.append(element)
print("The given list is: ", my_lst)

temp_lst1 = []
new_lst = []
for j in range(len(my_lst)):
    temp_lst1.append(my_lst[j])
    temp_lst2 = tuple(temp_lst1)
    new_lst.append(temp_lst2)
    temp_lst1 = []
print("The tuple of tuples will be: ", new_lst)
