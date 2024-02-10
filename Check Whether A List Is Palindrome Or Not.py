# Check Whether A List Is Palindrome Or Not...
lst = []
num = int(input("Enter the number of elements in the list: "))      # Taking The Number Of Elements In List
for i in range(1, num+1):
    lst.append(input("Enter the element number {}: ".format(i)))    # Taking Elements In List
print("The list will be: ", lst)
new_lst = list(reversed(lst))    # Reversing The List And Making A New List
if new_lst == lst:               # Checking The Condition
    print("The list is PALINDROME...")
else:
    print("The list is not PALINDROME...")
