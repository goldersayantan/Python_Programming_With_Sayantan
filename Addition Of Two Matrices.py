# Addition Of Two Matrices...
limit = int(input("Enter the order of the matrix: "))
print("For First Matrix: ")
mat1 = []
mat1_temp = []
for i in range(limit):
    for j in range(limit):
        element_for_first_matrix = int(input(f"Enter the element in {i+1}{j+1} index: "))
        mat1_temp.append(element_for_first_matrix)
    mat1.append(mat1_temp)
    mat1_temp = []

print("For Second Matrix: ")
mat2 = []
mat2_temp = []
for k in range(limit):
    for l in range(limit):
        element_for_second_matrix = int(input(f"Enter the element in {k+1}{l+1} index: "))
        mat2_temp.append(element_for_second_matrix)
    mat2.append(mat2_temp)
    mat2_temp = []

print("The matrix after addition will be: ")
for m in range(limit):
    for n in range(limit):
        print(mat1[m][n] + mat2[m][n], " ", end='')
    print("\n")
