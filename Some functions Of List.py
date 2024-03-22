# Some functions Of List...
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print("The given list is:", lst)

# insert()
insert_index = int(input("Enter the index to add element: "))
insert_element = int(input("Enter the element to add: "))
lst.insert(insert_index, insert_element)
print("The new list will be: ", lst)

# remove()
remove_element = int(input("Enter the element to be removed: "))
lst.remove(remove_element)
print("The list will be: ", lst)

# append()
append_element = int(input("Enter the element to add at the end of list: "))
lst.append(append_element)
print("The list will be: ", lst)

# len()
print("The length of the list is:", len(lst))

# pop()
del_index = int(input("Enter the index to delete element: "))
lst.pop(del_index)
print("The list will be: ", lst)

# clear()
print("After clearing the list, the list will be: ", lst.clear())
