# Write a Python program to merge two dictionaries...
my_dict1 = {}
limit1 = int(input("Enter the number of key-value pairs, you want in the first dictionary: "))
for i in range(limit1):
    key = input(f"Enter the key number {i + 1}: ")
    value = input(f"Enter the value number {i + 1}: ")
    my_dict1[key] = value
print("The dictionary will be: ", my_dict1)

my_dict2 = {}
limit2 = int(input("Enter the number of key-value pairs, you want in the second dictionary: "))
for j in range(limit2):
    key = input(f"Enter the key number {j + 1}: ")
    value = input(f"Enter the value number {j + 1}: ")
    my_dict1[key] = value
print("The dictionary will be: ", my_dict1)

print("The new dictionary will be: ", my_dict1.update(my_dict2))
