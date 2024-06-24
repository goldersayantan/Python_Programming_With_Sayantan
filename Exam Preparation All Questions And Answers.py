# # Access item in tuple...
# limit = int(input("Enter the number of elements you want to add in tuple: "))
# temp_lst = []
# for i in range(0, limit):
#     element = int(input(f"Enter the element in {i} index: "))
#     temp_lst.append(element)
# my_tup = tuple(temp_lst)
# print("The tuple will be: ", my_tup)
#
# index = int(input("Enter the index of the tuple, which you want to access: "))
# accessed_element = my_tup[index]
# print("You choose the element: ", accessed_element)
#
#
# # Addition Of Two Matrices...
# order = int(input("Enter the order of the matrix: "))
# print("For first matrix: ")
# first_temp_matrix = []
# first_original_matrix = []
# for i in range(0, order):
#     for j in range(0, order):
#         element1 = int(input(f"Enter the element in {i+1}{j+1} index: "))
#         first_temp_matrix.append(element1)
#     first_original_matrix.append(first_temp_matrix)
#
# print("For second matrix: ")
# second_temp_matrix = []
# second_original_matrix = []
# for i in range(0, order):
#     for j in range(0, order):
#         element2 = int(input(f"Enter the element in {i+1}{j+1} index: "))
#         second_temp_matrix.append(element2)
#     second_original_matrix.append(second_temp_matrix)
#
# print("The addition will be: ")
# for i in range(0, order):
#     for j in range(0, order):
#         print(first_original_matrix[i][j] + second_original_matrix[i][j], end=" ")
#     print("\n")
#
#
# # Append new string in the middle of the new string...
# first_str = input("Enter the first string: ")
# second_str = input("Enter the second string, which you want to add: ")
# length_of_first_str = len(first_str)
# print("The new string will be: ", first_str[0:length_of_first_str // 2] + second_str + first_str[length_of_first_str // 2:])
#
#
# # Calculating the permutation and combination...
# def factorial(x):
#     fact = 1
#     for i in range(1,x+1):
#         fact = fact*i
#     return fact
#
#
# def permutation(a,b):
#     return factorial(a) // factorial(a - b)
#
#
# def combination(a,b):
#     return factorial(a) // (factorial(b) * factorial(a - b))
#
#
# p = int(input("Enter the value of p: "))
# r = int(input("Enter the value of r: "))
# print("The permutation will be: ", permutation(p, r))
# print("The combination will be: ", combination(p, r))
#
#
# # Check a number is prime or composite...
# num = int(input("Enter a number to check if it is a prime number: "))
# prime = 0
# for i in range(2, num):
#     if num % i == 0:
#         prime = 0
#         break
#     else:
#         prime = 1
#
# if num == 0:
#     print("0 is not considered as a prime or composite number")
# elif num == 1:
#     print(f"{num} is neither prime nor a composite number")
# elif num == 2:
#     print(f"{num} is a prime number")
# elif num < 0:
#     print("Negative numbers are not considered as prime or composite numbers")
# elif prime == 0:
#     print(f"{num} is a composite number")
# else:
#     print(f"{num} is a prime number")
#
#
# # Check two numbers are amicable are not...
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# temp1 = num1
# total1 = 0
# temp2 = num2
# total2 = 0
# for i in range(1, temp1):
#     if temp1 % i == 0:
#         total1 = total1 + i
#
# for j in range(1, temp2):
#     if temp2 % j == 0:
#         total2 = total2 + j
#
# if total1 == num2 and total2 == num1:
#     print(f"{num1} and {num2} are amicable numbers")
# else:
#     print(f"{num1} and {num2} are not amicable numbers")
#
#
# # Check whether a list is palindrome or not...
# my_lst = []
# limit = int(input("Enter the number of elements you want: "))
# for i in range(limit):
#     element = input(f"Enter the element in {i} index: ")
#     my_lst.append(element)
# print("Your list is: ", my_lst)
# reversed_lst = list(reversed(my_lst))
# if my_lst == reversed_lst:
#     print("The list is palindrome list")
# else:
#     print("The list is not palindrome list")
#
#
# # Count the number of digits in a number...
# num = int(input("Enter a number: "))
# count = 0
# while num > 0:
#     num = num // 10
#     count += 1
#
# print("The number of digits is: ", count)
#
#
# # Create a dictionary from a list...
# my_lst = [[1, 'A'], [2, 'B'], [3, 'C']]
# my_dict = dict(my_lst)
# print("The dictionary will be: ", my_dict)
#
#
# # Create a list in which the number of sublist and the number of elements in every sublist will be of same number...
# limit = int(input("Enter the limit: "))
# my_lst = []
# for i in range(limit):
#     sub_lst = []
#     for j in range(limit):
#         sub_lst.append(j)
#     my_lst.append(sub_lst)
# print("The list will be: ", my_lst)
#
#
# # Create a user defined function with list and make sum of every alternate elements from that list...
# def sum_of_alternate_element(x):
#     total = 0
#     for i in range(len(x)):
#         if i % 2 != 0:
#             total = total + x[i]
#     return total
#
#
# limit = int(input("Enter the number of element you want to add in the list: "))
# my_lst = []
# for i in range(limit):
#     element = int(input(f"Enter the element in {i} index: "))
#     my_lst.append(element)
# print("The sum of every alternate element will be: ", sum_of_alternate_element(my_lst))
#
#
# # Create An User Defined Recursion Function Which Will Create A Table Of Number...
# def table_of_number(x, i=1):
#     if i <= 10:
#         print(f"{x} * {i} = {x * i}")
#         table_of_number(x, i+1)
#
#
# num = int(input("Enter a number to print the table: "))
# print("The table will be: ")
# table_of_number(num)
#
#
# # Create students that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average...
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def average(self):
#             total = 0
#             for i in self.marks:
#                 total += i
#             return total / len(self.marks)
#
#
# name = input("Enter your name: ")
# marks = []
# limit = int(input("Enter the number of subjects: "))
# for i in range(limit):
#     mark = int(input(f"Enter the marks of subject {i+1}: "))
#     marks.append(mark)
#
#
# s1 = Student(name, marks)
# print("Hi!", s1.name, "Your average marks is: ", s1.average())
#
#
# # Display the fibonacci series using function...
# def fibonacci(x):
#     temp1 = 0
#     temp2 = 1
#     while temp1 < x:
#         print(temp1)
#         temp1, temp2 = temp2, temp1 + temp2
#
#
# limit = int(input("Enter the limit: "))
# print("The fibonacci series will be: ")
# fibonacci(limit)
#
#
# # Table of numbers in a specific range...
# start_num = int(input("Enter the starting number: "))
# end_num = int(input("Enter the ending number: "))
# print("The table of numbers will be: ")
# for i in range(start_num, end_num+1):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print("---------------")
#
#
# # Taking input in dictionaries and printing it...
# my_dict = {}
# limit = int(input("Enter the number of key_value pair you want in dictionary: "))
# for i in range(limit):
#     key = input(f"Enter the key number {i + 1}: ")
#     value = input(f"Enter the value number {i + 1}: ")
#     my_dict[key] = value
#
# print("The dictionary will be: ")
# print(my_dict)
#
# -----------------------------------------------------------------------------------------------
#
# # Strings...
# my_str = "sayantan golderrr"
# print("The length of the string is: ", len(my_str))
# print("The string in uppercase will be: ", my_str.upper())
# print("The string in lowercase will be: ", my_str.lower())
# print("The string after trailing, will be: ", my_str.rstrip("r"))
# # print("After replacing: ", my_str.replace("a", "e"))
# print("After replacing: ", my_str.replace("Golderrr", "Golder"))
# print("After uppercasing the header, the string will be: ", my_str.capitalize())
# print("After centering the string, will be: ", my_str.center(50))
# print("There is: ", my_str.count("a"), "\"a\" in the string")
# print("is the string endswith r or not: ", my_str.endswith("r"))
# print("The index of the \"a\" is: ", my_str.index("a"))
# print("The index of \"a\" is: ", my_str.find("a", 8))     # "********************"
# # ^^^^ above function will print -1, when there is no character.
#
# # checking alphanumeric or not...
# new_str = ""
# print(new_str.isalnum())  # hcc123    (no special character or space)
# print(new_str.isalpha())  # abc    (only alphabets, no space or special characters)
# print(new_str.isdigit())  # Only numbers
# print(new_str.isspace())  # Only space
# print(new_str.isupper())  # There can be numbers with alphabets, only alphabet will check
# print(new_str.islower())  # ||
#
#
# List...
# my_lst1 = [50, 60, 40, 20, 10, 80, 70, 90, 100, 30]
# my_lst2 = ["Sayantan", "Susovan", "Namita"]
# my_lst1.sort()
# print(my_lst1)
# my_lst1.sort(reverse=True)
# print(my_lst1)
# my_lst1.reverse()
# print(my_lst1)
# sayantan_index = my_lst2.index("Sayantan")
# print("The word 'sayantan' in the list is in: ", sayantan_index, "index")
# print("The number 10 is in the list for: ", my_lst1.count(10), "times.")
# my_lst1.insert(10, 200)
# print(my_lst1)
# my_lst1.append(500)
# print(my_lst1)
# my_lst1.extend(my_lst2)
# print(my_lst1)
# print("The new list, after concatenation:", my_lst1 + my_lst2)
#
#
# Tuple...
# tup = (10, 20, 30, 40, 50, 60, 70, 80, 90)
# print(tup.index(20))
# print(tup.count(20))
#
#
# # Create a string made of first, middle and last character...
# my_str = input("Enter a string: ")
# print("The new string will be: ", my_str[0] + my_str[len(my_str) // 2] + my_str[-1])
#
# # Create a string made of the middle three character...
# my_str = input("Enter a string: ")
# print("The new string will be: ", my_str[(len(my_str) // 2) - 1] + my_str[len(my_str) // 2] + my_str[(len(my_str) // 2) + 1])
#
# # Append new string in the middle of a given string...
# my_str = input("Enter a string: ")
# new_str = input("Enter a new string: ")
# print("The required string will be: ", my_str[0:(len(my_str) // 2)] + new_str + my_str[(len(my_str) // 2):])
#
# # Create a string made of first, middle and last character of each given string...
# first_str = input("Enter the first string: ")
# second_str = input("Enter the second string: ")
# third_str = input("Enter the third string: ")
# print("The new string will be: ", first_str[0] + second_str[len(second_str) // 2] + third_str[-1])
#
# # Arrange string characters such that lowercase letters should come first...
# my_str = input("Enter a string: ")
# lower_str = ""
# upper_str = ""
# for i in range(len(my_str)):
#     if my_str[i].islower():
#         lower_str = lower_str + my_str[i]
#     else:
#         upper_str = upper_str + my_str[i]
#
# print("the string will be: ", lower_str + upper_str)
#
#
# # Count all letters, digits and special characters from a given string...
# my_str = input("Enter a string: ")
# lowercase_letters_count = 0
# uppercase_letters_count = 0
# digits_count = 0
# special_characters_count = 0
# spaces_count =0
#
# for i in range(len(my_str)):
#     if my_str[i].islower():
#         lowercase_letters_count += 1
#     elif my_str[i].isupper():
#         uppercase_letters_count += 1
#     elif my_str[i].isdigit():
#         digits_count += 1
#     elif my_str[i].isspace():
#         spaces_count += 1
#     else:
#         special_characters_count += 1
#
# print("Total count of lowercase letters: ", lowercase_letters_count)
# print("Total count of uppercase letters: ", uppercase_letters_count)
# print("Total count of digits: ", digits_count)
# print("Total count of special characters: ", special_characters_count)
# print("Total count of spaces: ", spaces_count)
#
#
# # Add two numbers...
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("the addition will be: ", num1 + num2)
#
#
# # Write a python program to find remainder when a number divided by 2...
# num = int(input("Enter a number: "))
# divider = int(input("Enter the divider: "))
# if divider == 2:
#     print("The remainder is: ", num % divider)
#
#
# # Check the type of the variable assigned using input() function...
# temp_var = input("Enter something: ")
# print("The type of the variable is: ", type(temp_var))
#
#
# # Use comparison operators to find out whether a given variable 'a' is greater than 'b' or not...
# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# if a > b:
#     print(f"{a} is greater than {b}")
# elif b > a:
#     print(f"{b} is greater than {a}")
# else:
#     print(f"{a} and {b} are equal")
#
#
# # Write a python program to find the average of two numbers entered by the user...
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print("The average is: ", (num1 + num2) // 2)
#
#
# # Write a python program to find the square of number entered by the user...
# num = int(input("Enter the number: "))
# print("The square of the entered number is: ", num**2)
#
#
# # Write a python program to display user entered name followed by "Good Afternoon" using input function...
# name = input("Enter your name: ")
# print(f"Good Morning {name}")
#
#
# # Write a python program to fill in a letter template below with name and date...
# name = input("Enter your name: ")
# date = input("Enter the date: ")
# print(f"""Dear <|{name}|>,\nYou are selected!\n<|{date}|>""")
#
#
# # Write a program to detect double spaces in the string...
# my_str = input("Enter a string to find the double space in the string: ")
# double_space = False
# if "  " in my_str:
#     double_space = True
# else:
#     double_space = False
# if double_space:
#     print("Double space detected in the given string.")
# else:
#     print("Double space does not detected in the given string.")
#
#
# # Replace the double space with the single space...
# my_str = input("Enter a string: ")
# double_space = False
# if "  " in my_str:
#     double_space = True
# else:
#     double_space = False
# if double_space:
#     print("Double space found")
#     my_str = my_str.replace("  ", " ")
#     print("After changing the 'double space' with 'single space' the string will be: ", my_str)
#
#
# # Write a program in python to format the following letter using escape sequence characters...
# letter = "Dear Harry,\n\tThis python course is nice.\n\t\t\t\t\t\tThanks!"
# print(letter)
#
#
# # Write a program to store seven fruits in a list entered by the user...
# limit = int(input("Enter the number of fruits you want to enter the list: "))
# fruits = []
# for i in range(limit):
#     fruit = input(f"Enter the fruit number {i + 1}: ")
#     fruits.append(fruit)
# print("The list will be: ", fruits)
#
#
# # Write a program to accept marks of 6 students and display them in a sorted manner...
# marks = []
# for i in range(1, 7):
#     mark = int(input(f"Enter the marks of student {i}: "))
#     marks.append(mark)
# marks.sort()
# print("The list of marks after sorting will be: ", marks)
#
#
# # Write a program to sum a list with 4 numbers...
# limit = int(input("Enter the limit of number you want to add in the list: "))
# my_lst = []
# for i in range(limit):
#     element = int(input(f"Enter the element number {i + 1}: "))
#     my_lst.append(element)
# print("The list is: ", my_lst)
# print("The sum will be: ", sum(my_lst))
#
#
# # Write a program to count the number of zeroes:
# my_tup = (7, 0, 8, 0, 0, 9)
# print("The count of 0 is: ", my_tup.count(0))
#
#
# # Write a program to create a dictionary of hindi words with values as their english translation. Provide user with an option to look it up...
# my_dict = {}
# limit = int(input("Enter the number of key-value pairs you want in dictionary: "))
# for i in range(limit):
#     key = input(f"Enter the key number {i}: ")
#     value = input(f"Enter the value for \"{key}\": ")
#     my_dict[key] = value
# print("The given dictionary is: ", my_dict)
# key_for_value = input("Enter the key to find value: ")
# print("The value is: ", my_dict.get(key_for_value))
#
#
# # write a program to input eight numbers from the user and display all the unique numbers(once)...
# temp_lst = []
# limit = int(input("Enter the number of elements you want: "))
# for i in range(limit):
#     element = input(f"Enter the element number {i + 1}: ")
#     temp_lst.append(element)
# my_set = set(temp_lst)
# print("The set with unique numbers will be: ", my_set)
#
#
# # Can we have a set with 18(int) and "18"(str) as a values in it?
# my_set = (18, "18")
# print(my_set)
# # Answer will be yes.
#
#
# # What will be the length of following set S...
# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(s)
# print(len(s))
#
#
# # type...
# s = {}
# print(type(s))
#
#
# # Create an empty dictionary. Allow 4 friends to enter their favourite languages values and use keys as their names.
# # Assume that the names are unique...
# my_dict = {}
# limit = int(input("Enter the number of friends you have: "))
# for i in range(limit):
#     name = input("Enter the name for friend {i + 1}: ")
#     fav_lang = input("Enter their favourite language: ")
#     my_dict[name] = fav_lang
# print("The dictionary is: ", my_dict)
#
#
# Write a program to find greatest of four numbers entered by the user...
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# num4 = int(input("Enter the fourth number: "))
# if num1 > num2 and num1 > num3 and num1 > num4:
#     print(f"{num1} is greater")
# elif num2 > num1 and num2 > num3 and num2 > num4:
#     print(f"{num2} is greater")
# elif num3 > num1 and num3 > num2 and num3 > num4:
#     print(f"{num3} is greater")
# elif num4 > num1 and num4 > num2 and num4 > num3:
#     print(f"{num4} is greater")
# else:
#     print("All numbers are same")
#
#
# # Write a program to find out whatever a student is pass or fail, if it requires total 40% and at least 33% in each
# # subject to pass. Assume 3 subjects and take marks as an input from the user...
# name = input("Enter your name: ")
# subject_limit = int(input("Enter the subject limit: "))
# subject_lst = []
# print("Enter the marks out of 100:")
# for i in range(subject_limit):
#     subject_marks = int(input(f"Enter the marks of subject {i + 1}: "))
#     subject_lst.append(subject_marks)
# total_percentage = sum(subject_lst) / len(subject_lst)
# fail = 0
# if total_percentage < 40:
#     print(f"{name}! You are failed in exam.")
# elif total_percentage >= 40:
#     for i in range(len(subject_lst)):
#         if subject_lst[i] < 33:
#             fail = 1
#             break
#         else:
#             fail = 0
#
#     if fail == 0:
#         print(f"{name}! You are passed in exam.")
#     else:
#         print(f"{name}! You are failed in exam.")
# else:
#     print("An error occurred")
#
#
# # write a program to find whether a given username contains less than 10 characters or not...
# username = input("Enter your username: ")
# if len(username) < 10:
#     print("username contains less than 10 characters")
# elif len(username) == 10:
#     print("username contains exact 10 characters")
# else:
#     print("username contains more than 10 characters")
#
#
# # Write a program which finds out whether a given name is present in a list or not...
# name_limit = int(input("Enter the limit of name, you want to include in your list: "))
# name_list = []
# for i in range(name_limit):
#     name = input(f"Enter the name of person number {i + 1}: ")
#     name_list.append(name)
# find_name = input("Enter the name to check in list: ")
# found = 0
# for i in range(len(name_list)):
#     if name_list[i] == find_name:
#         found = 1
#         break
#     else:
#         found = 0
# if found == 0:
#     print(f"\"{find_name}\" name not found in list.")
# else:
#     print(f"\"{find_name}\" name found in list.")
#
#
# # Write a program to calculate the grade of a student from his marks from the following scheme:
# """
# 90 - 100 -> Ex
# 80 - 90 -> A
# 70 - 80 -> B
# 60 - 70 -> C
# 50 - 60 -> D
# < 50 -> F
# """
# try:
#     marks = int(input("Enter marks: "))
#     if marks <= 100 and marks > 90:
#         print("The grade is Ex.")
#     elif marks <= 90 and marks > 80:
#         print("The grade is A.")
#     elif marks <= 80 and marks > 70:
#         print("The grade is B.")
#     elif marks <= 70 and marks > 60:
#         print("The grade is C.")
#     elif marks <= 60 and marks > 50:
#         print("The grade is D.")
#     elif marks <=50:
#         print("The grade is F.")
#     else:
#         print("Invalid Marks")
# except Exception as e:
#     print(e)
#
#
# # Write a program to find whether a post is taking about harry or not...
# post = input("Enter a post: ")
# post_str = post.lower()
# if "harry" in post_str:
#     print("This post is taking about harry.")
# else:
#     print("This post is not taking about harry.")
#
#
# # Write a program to print the multiplication table of a number...
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} X {i} = {num * i}")
#
#
# # Write a program to print the multiplication table of numbers in a specific range...
# start_num = int(input("Enter the starting number: "))
# stop_num = int(input("Enter the ending number: "))
# for i in range(start_num, stop_num + 1):
#     for j in range(1, 11):
#         print(f"{i} X {j} = {i * j}")
#     print("-------------")
#
#
# # write a program to greet all the people given in the list...
# lst = ["Harry", "Soham", "Sachin", "Rahul"]
# name = input("Enter your name: ")
# found = 0
# for i in lst:
#     if i == name:
#         found = 1
#         break
#     else:
#         found = 0
# if found == 1:
#     print(f"Welcome, {name}")
# else:
#     print(f"Sorry, {name}. You are not in list")
#
#
# # Write a program to print the multiplication table of numbers in a specific range using while loop...
# num = int(input("Enter a number: "))
# i = 1
# while i < 11:
#     print(f"{num} X {i} = {num * i}")
#     i = i + 1
#
#
# # Write a program to check whether a number is prime or not...
# num = int(input("Enter a number: "))
# prime = 0
# for i in range(2, num):
#     if num % i == 0:
#         prime = 0
#         break
#     else:
#         prime = 1
#
# if num == 0 or num == 1:
#     print(f"{num} is neither a prime number nor a composite number")
# elif num == 2:
#     print("2 is a prime number")
# elif num < 0:
#     print(f"{num} is neither a prime number nor a composite number")
# elif prime == 1:
#     print(f"{num} is a prime number")
# elif prime == 0:
#     print(f"{num} is a composite number")
# else:
#     print("Invalid input")
#
#
# # Write a program to find the sum of first n natural numbers using for loop...
# limit = int(input("Enter the limit of the number: "))
# total = 0
# for i in range(1, limit+1):
#     total = total + i
# print("The sum of first n natural number: ", total)
#
#
# # Write a program to find the sum of first n natural numbers using while loop...
# limit = int(input("Enter the limit of number: "))
# total = 0
# while limit > 0:
#     total = total + limit
#     limit = limit - 1
# print("The sum of first n natural number: ", total)
#
#
# # Write a program to calculate the factorial of a given number using for loop...
# number = int(input("Enter a number to find the factorial: "))
# fact = 1
# for i in range(number, 0, -1):
#     fact = fact * i
# print(f"The factorial of {number} is: ", fact)
#
#
# # Write a program to print the following star pattern...
#    *
#   ***
#  *****
# *******
# line = int(input("Enter the number of lines you need to print the *: "))
# for i in range(1, line + 1):
#     for j in range(line - i):
#         print(" ", end="")
#     for k in range((2 * i) - 1):
#         print("*", end="")
#     print()
#
#
# # Write a program to print the following star pattern...
# *
# **
# ***
# limit = int(input("Enter the number of line: "))
# for i in range(1, limit+1):
#     print("*" * i)
# limit = int(input("Enter the number of line: "))
# for i in range(1, limit+1):
#     for j in range(i):
#         print("*", end="")
#     print()
#
#
# # Write a program to print multiplication table of a number using for loop in reversed order.
# num = int(input("Enter the number: "))
# for i in range(10, 0, -1):
#     print(f"{num} X {i} = {num * i}")
#
#
# # Write a program using function to find greatest of three numbers...
# def greatest_three_num(x, y, z):
#     if x > y and x > z:
#         print(f"{x} is greatest")
#     elif y > x and y > z:
#         print(f"{y} is greatest")
#     elif z > x and z > y:
#         print(f"{z} is greatest")
#     elif x > y and x == z:
#         print(f"{x} is greatest")
#     elif y > x and y == z:
#         print(f"{y} is greatest")
#     elif z > x and z == y:
#         print(f"{z} is greatest")
#     elif x ==y and y == z:
#         print("All numbers are same")
#     else:
#         print("Invalid")
#
#
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# greatest_three_num(num1, num2, num3)
#
#
# # Write a program using function to convert Celsius to Fahrenheit...
# def cel_to_far(c):
#     return ((9 * c) + 160) / 5
#
#
# cel = float(input("Enter the temperature in celsius: "))
# print(f"{cel} in fahrenheit will be: {cel_to_far(cel)}")
#
#
# # How do you prevent a python print() function to print a new line at the end...
# print("Hello World", end=" ")
# print("How are you?")
#
#
# # Write a recursive function to calculate the sum of first n natural number...
# def sum_natural_number(x):
#     if x == 0:
#         return 0
#     else:
#         return x + sum_natural_number(x-1)
#
#
# num = int(input("Enter the limit of the number: "))
# print("The sum of n natural numbers is:", sum_natural_number(num))
#
#
# # Write a python function to print first n lines of the following pattern...
# def left_triangle(x):
#     for i in range(x, 0, -1):
#         print("*" * i)
#
#
# line = int(input("Enter the number of lines: "))
# left_triangle(line)
# def left_triangle(x):
#     for i in range(x, 0, -1):
#         for j in range(i):
#             print("*", end="")
#         print()
#
#
# line = int(input("Enter the number of lines: "))
# left_triangle(line)
#
#
# # Write a function to convert inches to cms...
# def inchToCm(x):
#     return x * 2.54
#
#
# inch = int(input("Enter the length in inches: "))
# print("The length in cm will be: ", inchToCm(inch))
#
#
# # Write a python function to remove a given word from a list and stop it at the same time...
# def remove_element(x):
#     remove_ele = input("Enter the element which you want to remove: ")
#     element_found = 0
#     for j in range(len(my_lst)):
#         if remove_ele == my_lst[j]:
#             element_found = 1
#             break
#         else:
#             element_found = 0
#
#     if element_found == 0:
#         print("Element not found")
#     else:
#         index = my_lst.index(remove_ele)
#         print("Element removed")
#         print("The new list will be: ", my_lst[0:index])
#
#
# limit = int(input("Enter the number of elements you want to add in list: "))
# my_lst = []
# for i in range(limit):
#     element = input(f"Enter the element number {i}: ")
#     my_lst.append(element)
# print("Your list will be: ", my_lst)
# remove_element(my_lst)
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#
# s1 = Student("Sayantan", 100)
# print(s1.name)
# print(s1.marks)
#
# class Student:
#     def __init__(self):
#         print("Hello World")
#
#
# s1 = Student()
#
#
# # Create a class programmer to store the information of few programmers working at Microsoft...
# class Programmer:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#
# Microsoft_programmer = Programmer
# p1 = Microsoft_programmer("Sayantan Golder", 18, 10000000)
# print(p1.name)
# print(p1.age)
# print(p1.salary)
#
#
# # Write a class calculator, capable of finding square and squareroot of a number...
# import math
# class Calculator:
#     @staticmethod
#     def square(number):
#         return number ** 2
#
#     @staticmethod
#     def cube(number):
#         return number ** 3
#
#     @staticmethod
#     def squareroot(number):
#         return math.sqrt(number)
#
#
# calculation = Calculator()
# num = int(input("Enter a number: "))
# print(f"The square of {num} will be: ", calculation.square(num))
# print(f"The cube of {num} will be: ", calculation.cube(num))
# print(f"The squareroot of {num} will be: ", calculation.squareroot(num))
#
#
# # Create a class with a class attribute a; create an object from it and set a directly using object.a = 0,
# # Does this change the class attribute?
# class Tempclass:
#     def __init__(self, a):
#         self.a = a
#
#
# obj1 = Tempclass(1)
# print(obj1.a)
# obj1.a = 0
# print(obj1.a)         # Yes it changes
#
#
# # Add a static method to greet the user with "Hello, name"...
# import math
#
#
# class Calculator:
#     @staticmethod
#     def square(number):
#         return number ** 2
#
#     @staticmethod
#     def cube(number):
#         return number ** 3
#
#     @staticmethod
#     def squareroot(number):
#         return math.sqrt(number)
#
#     @staticmethod
#     def greet(name):
#         print(f"Welcome {name}!")
#
#
# calculation = Calculator()
# name = input("Enter your name: ")
# num = float(input("Enter the number: "))
# calculation.greet(name)
# print(f"The square of {num} is: ", calculation.square(num))
# print(f"The cube of {num} is: ", calculation.cube(num))
# print(f"The squareroot of {num} is: ", calculation.squareroot(num))
#
#
# # Write a class Train which has method to book a ticket, get status(no of seats) and get fare information of trains...
# class Train:
#     def __init__(self, train_name, train_number, total_seats, train_fare):
#         self.train_name = train_name
#         self.train_number = train_number
#         self.total_seats = total_seats
#         self.available_seats = total_seats
#         self.train_fare = train_fare
#         self.bookings = []
#
#     def train_seat_bookings(self, passenger_name):
#         if self.total_seats > 0:
#             self.bookings.append(passenger_name)
#             self.available_seats -= 1
#             return f"Ticket booked for: {passenger_name}, seat number is: {self.total_seats - self.available_seats}"
#         else:
#             return "No seats available"
#
#     def get_status(self):
#         return f"Available seats: {self.available_seats} / {self.total_seats}"
#
#     def get_fare_status(self):
#         return f"Fare per ticket: {self.train_fare}"
#
#
# train = Train("Super Express", 12345, 100, 500)
# print(train.get_status())
# print(train.get_fare_status())
# print(train.train_seat_bookings("Alex"))
# print(train.train_seat_bookings("Bob"))
# print(train.get_status())
#
#
# txt = "The best things in life are free!"
# print("free" in txt)
#
#
# txt = "The best things in life are free!"
# print("expensive" not in txt)
#
#
# b = "Hello, World!"
# print(b[2:15])
#
#
# # Create a class pets from a class Animals and further create class dog from pets. Add a method bark to class dog...
# class Animals:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# class Pets(Animals):
#     def __init__(self, name, owner):
#         super().__init__(name)
#         self.owner = owner
#
#     def get_owner(self):
#         return self.owner
#
#
# class Dogs(Pets):
#     def __init__(self, name, owner, breed):
#         super().__init__(name, owner)
#         self.breed = breed
#
#     def bark(self):
#         return "Woof! Woof"
#
#     def get_breed(self):
#         return self.breed
#
#
# my_dog = Dogs("Buddy", "Sayantan Golder", "Golden Retriever")
# print(f"My dog name is: {my_dog.get_name()}")
# print(f"My dog breed: {my_dog.get_breed()}")
# print(f"My dog owner is: {my_dog.get_owner()}")
# print(f"My dog says: {my_dog.bark()}")
#
#
# # Write a python program to take a number from the user and check whether it is greater or smaller than a + (a / 2)...
# num = int(input("Enter a number: "))
# temp_num = num + (num / 2)
# if temp_num > num:
#     print(f"{num} is less than {temp_num}")
# elif temp_num < num:
#     print(f"{num} is greater than {temp_num}")
# else:
#     print("Both numbers are equal")
#
#
# # Wap to take 2 input from the user as a * b to solve. The algebraic equation (a+b)^3...
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# print("(a + b)^3 = ", (a + b) ** 3)
#
#
# # Input a number of 5 digit and find difference between odd and even digit(using while loop)...
# num = int(input("Enter a number: "))
# odd_nums = 0
# even_nums = 0
# while num > 0:
#     temp_num = num % 10
#     num = num // 10
#     if temp_num % 2 == 0:
#         even_nums = even_nums + temp_num
#     else:
#         odd_nums = odd_nums + temp_num
# if odd_nums > even_nums:
#     print(f"The difference between odd and even number is: {odd_nums - even_nums}")
# elif even_nums > odd_nums:
#     print(f"The difference between even and odd number is: {even_nums - odd_nums}")
# else:
#     print("There is no difference between odd and even number.")
#
#
# # Wap to add two tuple t1, t2 using function...
# def add_two_tuple(t1, t2):
#     temp_lst = []
#     for i in range(len(t1)):
#         element = t1[i] + t2[i]
#         temp_lst.append(element)
#     return temp_lst
#
#
# limit = int(input("Enter the number of elements you want in the tuple: "))
# temp_tup1 = []
# temp_tup2 = []
# for i in range(limit):
#     ele = int(input(f"Enter the element number {i + 1}: "))
#     temp_tup1.append(ele)
# tup1 = tuple(temp_tup1)
# print("The first tuple is: ", tup1)
#
# for j in range(limit):
#     ele = int(input(f"Enter the element number {j + 1}: "))
#     temp_tup2.append(ele)
# tup2 = tuple(temp_tup2)
# print("The second tuple is: ", tup2)
# print("After adding two tuples, the new tuple will be: ", add_two_tuple(tup1, tup2))
#
#
# # Wap to add tuple t1, t2 using function where t1 is outside the function and t2 is inside the function...
# def add_two_tuple(tup2):
#     lim = int(input("Enter the number of elements you want in the second tuple: "))
#     temp_tup = []
#     for i in range(lim):
#         ele = int(input(f"Enter the element number {i + 1}: "))
#         temp_tup.append(ele)
#     tup2 = tuple(temp_tup)
#     print("The first tuple is: ", tup2)
#
#     temp_lst = []
#     for i in range(len(temp_tup)):
#         element = tup2[i] + tup2[i]
#         temp_lst.append(element)
#     new_tup = tuple(temp_lst)
#     print("After adding two tuple the new tuple will be: ", new_tup)
#
#
# limit = int(input("Enter the number of elements you want in the first tuple: "))
# temp_tup1 = []
# for j in range(limit):
#     ele = int(input(f"Enter the element number {j + 1}: "))
#     temp_tup1.append(ele)
# tup1 = tuple(temp_tup1)
# print("The second tuple is: ", tup1)
# add_two_tuple(tup1)
#
#
# # Wap to change the tuple from (1, 2, 3, 4) to (100, 2, 3, 4)
# my_tup = (1, 2, 3, 4)
# temp_lst = list(my_tup)
# temp_lst[0] = 100
# new_tup = tuple(temp_lst)
# print("The new tuple will be: ", new_tup)
#
#
# # Wap to find the subset of a list...
# my_lst = []
# limit = int(input("Enter the number of elements you want in the list: "))
# for i in range(limit):
#     element = input(f"Enter the element number {i + 1}: ")
#     my_lst.append(element)
# print("The list will be: ", my_lst)
# print("The sub lists will be: ")
# my_lst.sort()
# sub_lst = []
# for i in range(len(my_lst)):
#     for j in range(i+1, len(my_lst)+1):
#         sub_lst.append(my_lst[i:j])
# print(sub_lst)
#
# # How to swap two numbers in python...
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num1 = num1 + num2
# num2 = num1 - num2
# num1 = num1 - num2
# print("The first number is: ", num1)
# print("The second number is: ", num2)