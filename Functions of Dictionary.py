# Given Dictionary...
my_dict = {
    "FIRST NAME": "Sayantan",
    "SUR NAME": "Golder",
    "SGPA": 8.95,
    "COURSE": "BCA",
    "ROLL NO.": "UG/02/BCA/2023/059",
    "REG. NO.": "AU/2023/0009576",
    "SUB AND GRADE": {
        "OPEN SOURCE SOFTWARE": "A",
        "INTRODUCTION TO PROGRAMMING LAB": "A",
        "COMMUNICATIVE ENGLISH-I": "A",
        "OPEN SOURCE SOFTWARE LAB": "O",
        "ENVIRONMENTAL EDUCATION": "A",
        "MATHEMATICS-I": "O",
        "ACADEMIC AND PROFESSIONAL WRITING: AN INTRODUCTION": "A+",
        "INTRODUCTION TO PROGRAMMING": "O"
    },
    "SCHOOL": "SCHOOL OF ENGINEERING AND TECHNOLOGY",
    "UNIVERSITY": "ADAMAS UNIVERSITY"
}

# Printing The Dictionary...
print("The dictionary is: \n", my_dict)

# Printing All The Keys Of The Dictionary...
print("All the keys of dictionary are: ", my_dict.keys())

# Printing All The values Of The key Of The Dictionary...
print("All the values Of The Dictionary are: ", my_dict.values())

# Printing All The (key, value) Pairs As Tuples...
print("All (key, values) Of The Dictionary are: ", my_dict.items())

# Printing The Key According To Value...
print("All The key according to value are: \n")
print(my_dict.get("FIRST NAME"))
print(my_dict.get("SUR NAME"))
print(my_dict.get("SGPA"))
print(my_dict.get("COURSE"))
print(my_dict.get("ROLL NO."))
print(my_dict.get("REG. NO."))
print(my_dict.get("SUB AND GRADE"))
print(my_dict.get("SCHOOL"))
print(my_dict.get("UNIVERSITY"))

# Inserts The Specified Items To The Dictionaries...
keys = input("Enter the key: ")
values = input("Enter the value: ")
my_dict.update({keys: values})
print("The new dictionary is: ", my_dict)

# Working.....
