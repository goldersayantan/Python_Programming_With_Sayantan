# Taking input a string...
s = str(input("Enter a string: "))
first_char = s[0]   # First character
middle_char = s[len(s)//2]  # Middle character
last_char = s[-1]   # Last character

# Printing Of string...
print("The string with first, middle and last character will be: ", first_char+middle_char+last_char)
