# Write a Python program to convert a tuple to a string...
limit = int(input("Enter the number of words yo want in tuple: "))
temp_lst = []
for i in range(limit):
    word = input(f"Enter the word number {i + 1}: ")
    temp_lst.append(word)
my_tup = tuple(temp_lst)
print("The tuple is: ", my_tup)

sentence = ""
for j in range(len(my_tup)):
    sentence = sentence + my_tup[j] + " "
print("the sentence will be: ", sentence)
