print("Using list combine 2 matrix.")
mat1 = [2, 2, 4, 2]
mat2 = [3, 3, 5, 6]
new_matrix = []
print("Matrix 1: ", mat1)
print("Matrix 2: ", mat2)
print()
for i in mat1:
    new_matrix.append(i)
for i in mat2:
    new_matrix.append(i)
print("New Matrix: ")
for i in new_matrix:
    print(i, end = " ")
