# Access Item In Tuple...
tup1 = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print("The tuple is: ", tup1)
access_index = int(input("Enter the index, which you want to access: "))
access = 0
for i in range(0, len(tup1)):
    if i == access_index:
        access = 1
        break
    else:
        access = 0
if access == 1:
    print("You choose the element: ", tup1[access_index])
else:
    print("Invalid Index")
