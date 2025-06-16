print("Using list create 2D matrix.")
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
matrix = []

print("Enter elements in rows:")
for i in range(r):
    a = []
    print("Enter", c, "elements in", i+1, "row: ")
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)

print("Elements in matrix are:")
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end = " ")
    print()
