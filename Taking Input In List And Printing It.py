# Taking Input In List And Printing It...
lst = []
number_elements = int(input("Enter number of elements you want to add: "))
for i in range(0, number_elements):
    new_element = input("Enter the element number {}: ".format(i+1))
    lst.append(new_element)
print("The list will be: ", lst)
