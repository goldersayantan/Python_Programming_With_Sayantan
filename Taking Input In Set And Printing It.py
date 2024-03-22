# Taking Input In Set And Printing It...
my_set = set()
number_of_elements = int(input("Enter the number of elements you want to add in set: "))
for i in range(0, number_of_elements):
    add_element = input("Enter the element number {}: ".format(i+1))
    my_set.add(add_element)
print("The set will be: ", my_set)
