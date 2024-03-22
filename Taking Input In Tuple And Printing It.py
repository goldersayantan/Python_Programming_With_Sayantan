# Taking Input In Tuple And Printing It...
tup = ()
temp = list(tup)
number_of_elements = int(input("Enter the number of elements you want to add: "))
for i in range(0, number_of_elements):
    add_element = input("Enter the element number {}: ".format(i+1))
    temp.append(add_element)
new_tup = tuple(temp)
print("The new tuple will be: ", new_tup)
