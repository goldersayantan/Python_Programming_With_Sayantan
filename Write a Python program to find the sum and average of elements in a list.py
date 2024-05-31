# Write a Python program to find the sum and average of elements in a list.
my_lst = []
limit = int(input("Enter the number of elements you want to add in list: "))
for i in range(limit):
    element = int(input(f"Enter the element number {i + 1}: "))
    my_lst.append(element)
print("The list is: ", my_lst)
total = 0
for i in my_lst:
    total += i
print("The sum of all the elements in list is: ", total)
print("The average of all the elements in list is: ", total // len(my_lst))
