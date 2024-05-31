# Write a Python program to find the key with the maximum value...
my_dict = {}
limit = int(input("Enter the number of key-value pairs, you want in the dictionary: "))
for i in range(limit):
    key = input(f"Enter the key number {i + 1}: ")
    value = input(f"Enter the value number {i + 1}: ")
    my_dict[key] = value
print("The dictionary will be: ", my_dict)

max_key = max(my_dict, key=my_dict.get)
print("The maximum key in the dictionary is: ", max_key)
