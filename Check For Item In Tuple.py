# Check For Item In Tuple...
tup1 = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print("The tuple is: ", tup1)
check_item = int(input("Enter the element to be checked: "))
check = 0
for i in range(0, len(tup1)):
    if tup1[i] == check_item:
        check = 1
        break
    else:
        check = 0
if check == 1:
    print("The element found in index: ", i)
else:
    print("The element not found")
