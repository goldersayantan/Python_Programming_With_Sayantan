# Given two sets, write a Python program to find their union, intersection, and difference...
my_set1 = set()
my_set2 = set()
limit_first_set = int(input("Enter the number of elements in first set: "))
for i in range(limit_first_set):
    element = int(input(f"Enter the element number {i + 1}: "))
    my_set1.add(element)
print("The first set is: ", my_set1)

limit_second_set = int(input("Enter the number of elements in second set: "))
for j in range(limit_second_set):
    element = int(input(f"Enter the element number {j + 1}: "))
    my_set2.add(element)
print("The first set is: ", my_set2)
print("The union of two sets is: ", my_set1.union(my_set2))
print("The intersection of two sets is: ", my_set1.intersection(my_set2))
print("The difference between two sets is: ", my_set1.difference(my_set2))
