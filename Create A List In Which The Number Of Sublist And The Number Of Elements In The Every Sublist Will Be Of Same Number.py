# Create A List In Which The Number Of Sublist And The Number Of Elements In The Every Sublist Will Be Of Same Number...
limit = int(input("Enter the limit of elements: "))
my_list = []
for i in range(0, limit):
    sub_list = []
    for j in range(1, limit+1):
        sub_list.append(j)
    my_list.append(sub_list)
print("The list will be: ", my_list)
