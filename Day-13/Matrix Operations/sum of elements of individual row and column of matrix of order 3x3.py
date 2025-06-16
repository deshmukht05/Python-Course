import numpy as np
print("Sum of elements of individual row and column of matrix of order 3x3")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original array: \n", arr)

for i in range(3):
    rs = 0
    for j in range(3):
        rs += arr[i][j]
    print("Sum of row ", i+1, "is: ", rs)

for j in range(3):
    cs = 0
    for i in range(3):
        cs += arr[i][j]
    print("Sum of columns ",j+1, "is: ", cs)