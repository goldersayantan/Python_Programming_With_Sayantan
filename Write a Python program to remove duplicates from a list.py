# 3. Write a Python program to remove duplicates from a list.
my_lst = []
limit = int(input("Enter the number of elements you want to add in the list: "))
for i in range(limit):
    element = int(input(f"Enter the element number {i + 1}: "))
    my_lst.append(element)
print("The given list is: ", my_lst)

temp_set = set(my_lst)
new_lst = list(temp_set)
print("The new_list without duplicate element is: ", new_lst)
