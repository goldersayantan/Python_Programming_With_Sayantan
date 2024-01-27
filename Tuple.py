# Making of a tuple...
num1 = int(input("Enter the number of elements in the tuple: "))
tup = ()
# Converting tuple into list...
temp = list(tup)
for i in range(num1):
    number = input("Enter the element in index no.{}: ".format(i))
    temp.append(number)
# converting list into tuple...
tup = tuple(temp)
print("The tuple is: ", tup)

# Any work for tuple:
        # Convert the tuple into list
        # Do some works
        # Convert the list into tuple
        
