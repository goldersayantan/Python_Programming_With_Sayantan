# Operation with Lists...
# Taking the number of elements in list...
num = int(input("Enter the number of elements in a list: "))
lst = []
for i in range(num):
    number = input("Enter the element in index {}: ".format(i))  # Taking elements in list...
    lst.append(number)
print("The original list is:", lst)

# The list in ascending order...
print("The sorted list is:", sorted(lst))

# The list in reverse order...
print("The list in reverse is: ", list(reversed(lst)))

# Check any character's index...
val1 = input("Enter the element to find index value: ")
if val1 in lst:
    print("The element (first occurrence) is in index no.: ", lst.index(val1))
else:
    print("There is no such element in the list")

# Check any character's occurrence...
val2 = input("Enter the element to find occurrence value:")
if val2 in lst:
    print("The element is in lst for: ", lst.count(val2), "times")
else:
    print("There is no such element in the list")

# Making a copy of original list...
temp = lst.copy()
print("The copy of original list is:", temp)

# Insert a new value to an index...
val3 = input("Enter the element to insert: ")
ind3 = int(input("Enter the element of index to insert the number {}: ".format(val3)))
lst.insert(ind3, val3)
print("The new list is:", lst)

# Adding a new element to the list at the end...
val4 = input("Enter the element to insert at last of the list: ")
lst.append(val4)
print("The list with added element is:", lst)

# Extend a list with a new list...
num2 = int(input("Enter the number of elements in the new list to insert: "))
lst_temp = []
for j in range(num2):
    number2 = (input("Enter the element in index {}: ".format(j)))
    lst_temp.append(number2)
lst.append(lst_temp)  # We can also do lst+lst_temp
print("The old list with new list is:", lst)

# Print the elements of the list in a specific range...
start1 = int(input("Enter the starting index: "))
stop1 = int(input("Enter the ending index: "))
# If we want to give steps in every iteration we can write lst[start1:stop1:step]
print("The required list from index", start1, "to", stop1, "is:", lst[start1:stop1])


# Taking values in list in a specific range...
start2 = int(input("Enter the starting number: "))
stop2 = int(input("Enter the ending number: "))
temp = [i for i in range(start2, (stop2+1))]
print(temp)

# We can give condition in list...
start3 = int(input("Enter the starting number: "))
stop3 = int(input("Enter the ending number: "))
temp = [i for i in range(start3, (stop3+1)) if i % 2 == 0]
print(temp)

# If we give any other variable instead of first i, and defined this variable with a number or character,
# it will be printed manually...
