# Count A String Has Odd Or Even Number Of Characters...
st = input("Enter a string: ")
if len(st) == 0:
    print("This String has no character.")
elif len(st) % 2 == 0:
    print("This String has even numbers of characters.")
elif len(st) % 2 != 0:
    print("This String has odd numbers of characters.")
else:
    print("Invalid String")
