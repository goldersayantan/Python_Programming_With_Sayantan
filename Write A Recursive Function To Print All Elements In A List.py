# Write A Recursive Function To Print All Elements In A List...
def lt(x, i=0):
    if i == len(x):
        return
    print(x[i])
    lt(x, i+1)


l = ["apple", "banana", "cherry", "orange", "pear", "orange"]
lt(l)
