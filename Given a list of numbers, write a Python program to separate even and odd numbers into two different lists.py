# Given a list of numbers, write a Python program to separate even and odd numbers into two different lists...
my_lst = []
limit = int(input("Enter the number of elements in the list: "))
for i in range(limit):
    element = int(input(f"Enter the element number {i + 1}: "))
    my_lst.append(element)
print("The given list is: ", my_lst)

odd_number_lst = []
even_number_lst = []
for i in range(len(my_lst)):
    if my_lst[i] % 2 == 0:
        even_number_lst.append(my_lst[i])
    else:
        odd_number_lst.append(my_lst[i])

print("The list with odd numbers is: ", odd_number_lst)
print("The list with even numbers is: ", even_number_lst)
