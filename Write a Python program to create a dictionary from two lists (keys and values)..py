# Write a Python program to create a dictionary from two lists (keys and values)...
key_lst = []
value_lst = []
limit = int(input("Enter the number of key-value pairs you want in your dictionaries: "))
for i in range(limit):
    key = input(f"Enter the key number {i + 1}: ")
    key_lst.append(key)
for j in range(limit):
    value = input(f"Enter the value number {j + 1}: ")
    value_lst.append(value)
my_dict = dict(zip(key_lst, value_lst))
print("the dictionary will be: ", my_dict)
