# Taking Input In Dictionaries And Printing It...
my_dict = {}
number_of_elements = int(input("Enter the number of elements you want to add in dictionary: "))
for i in range(0, number_of_elements):
    input_key = input("Enter the key number {}: ".format(i+1))
    input_value = input("Enter the value which is associated with key{}: ".format(i+1))
    my_dict[input_key] = input_value
print("The dictionary will be: ", my_dict)
