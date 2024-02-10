# Functions Of Strings...
# Taking A String...
st1 = str(input("Enter a string: "))

# Printing The Entire String...
print("Your string is:", st1)

# Calculating Length Of String...
print("The length of the string is:", len(st1))

# Concatenation Of Two Strings...
st2 = str(input("Enter another to concatenate: "))
new_string = st1 + st2
print("After Concatenation: \nThe string will be: ", new_string)

# Uppercasing The Entire String...
upp_string = new_string.upper()
print("The string in uppercase will be: ", upp_string)

# Lowercasing The Entire String...
low_string = new_string.lower()
print("The string in uppercase will be: ", low_string)

# Replacing Word Or Letter Or Substring From A string...
pre = str(input("Enter a letter or word or sub-string to be replace: "))
rep = str(input("Enter the new letter or word or sub-string: "))
print("After replacing: \nThe string will be: ", new_string.replace(pre, rep))

# Splitting String...
spl_str = str(input("Enter The string from where to split: "))
print("after splitting The new string will be: ", new_string.split(spl_str))   # It Will Create A List...

# Capitalize The First Letter...
print("After Capitalization: \nThe string will be: ", new_string.capitalize())

# Count The Occurrences of Any Letter Or Word Or Sub-string In The Entire String...
cou = str(input("Enter a letter or word or sub-string to count it's occurrences: "))
print("The occurrence is of", cou, "is: ", new_string.count(cou))

# Check If A Given Character Ends With A Given Character Or Word...
ends_with = str(input("Enter a letter or word or sub-string to check it ends the string or not: "))
if new_string.endswith(ends_with) is True:          # ends_with == new_string[-1]
    print("Yes, the string ends with the given character")
else:
    print("No, the string does not end with the given character")

# Find The First occurrence Of A Character In A String...
first_occur = str(input("Enter a letter or word or sub-string to find the first occurrence: "))
print("The first occurrence (The index) is: ", new_string.find(first_occur))


# Taking A New String...
stri = str(input("Enter a string: "))
if stri.isalnum() is True:
    print("The string is made of alphanumeric...")
if stri.isalpha() is True:
    print("The string is made of only alphabet")
if stri.isdigit() is True:
    print("The string is made of only digits")
if stri.islower() is True:
    print("The string is in lowercase")
if stri.isupper() is True:
    print("The string is in UPPERCASE")
if stri.istitle() is True:
    print("The string is in title case")
if stri.isspace() is True:
    print("The string is made of space")
else:
    print("Working...")
