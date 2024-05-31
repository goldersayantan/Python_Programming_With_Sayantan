# Write a Python program to find the symmetric difference between two sets.
my_set1 = set()
my_set2 = set()
limit_first_set = int(input("Enter the number of elements in the set: "))
for i in range(limit_first_set):
    element_of_first_set = int(input("Enter the element number {i + 1}: "))
    my_set1.add(element_of_first_set)
print("The first set is: ", my_set1)
limit_second_set = int(input("Enter the element number of elements in the set: "))
for j in range(limit_second_set):
    element_of_second_set = int(input("Enter the element number {j + 1}: "))
    my_set2.add(element_of_second_set)
print("The second set is: ", my_set2)
print("The symmetric difference between two sets is: ", my_set1.symmetric_difference(my_set2))
print("The symmetric difference between two sets is: ", my_set1 ^ my_set2)
