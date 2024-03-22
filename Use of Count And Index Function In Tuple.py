#  Write a python program using the following methods: 1) count 2) index...
tup1 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 50, 60, 30, 10, 90, 10, 50, 60, 30, 10)
occur_item = int(input("Enter a number to find occurrence: "))
print("The occurrence is: ", tup1.count(occur_item))

tup1 = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print("The given tuple is: ", tup1)
element = int(input("Enter the element to find the index value of the element: "))
print("The index is: ", tup1.index(element))
