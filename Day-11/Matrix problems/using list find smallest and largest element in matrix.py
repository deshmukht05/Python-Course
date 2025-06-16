print("Using list find smallest and largest element in matrix.")
n = int(input("Enter size of matrix: "))

mat = []
for i in range(0, n):
    ele = int(input("Enter elements: "))
    mat.insert(i, ele)
print("\nMatrix is: ")
for i in range(0, n):
    print(mat[i], end = " ")

print()

largest = max(mat)
l_index = mat.index(largest)
smallest = min(mat)
s_index = mat.index(smallest)
print(f"\n{largest} is largest with index value {l_index}")
print(f"\n{smallest} is smallest with index value {s_index}")
