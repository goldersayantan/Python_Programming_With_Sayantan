# Arrange string characters such that lowercase letters should come first...
my_str = input("Enter a string: ")
lower_str = ""
upper_str = ""
for i in range(len(my_str)):
    if my_str[i].islower():
        lower_str = lower_str + my_str[i]
    else:
        upper_str = upper_str + my_str[i]

print("the string will be: ", lower_str + upper_str)
