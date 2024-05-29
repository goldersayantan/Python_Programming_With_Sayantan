# Count all letters, digits and special characters from a given string...
my_str = input("Enter a string: ")
lowercase_letters_count = 0
uppercase_letters_count = 0
digits_count = 0
special_characters_count = 0
spaces_count =0

for i in range(len(my_str)):
    if my_str[i].islower():
        lowercase_letters_count += 1
    elif my_str[i].isupper():
        uppercase_letters_count += 1
    elif my_str[i].isdigit():
        digits_count += 1
    elif my_str[i].isspace():
        spaces_count += 1
    else:
        special_characters_count += 1

print("Total count of lowercase letters: ", lowercase_letters_count)
print("Total count of uppercase letters: ", uppercase_letters_count)
print("Total count of digits: ", digits_count)
print("Total count of special characters: ", special_characters_count)
print("Total count of spaces: ", spaces_count)
