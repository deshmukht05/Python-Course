print("Using list find sun of matric elements.")
n = int(input("Enter size of matrix: "))

if n==0:
    exit()
else:
    mat = []
    sum = 0
    for i in range(0, n):
        ele = int(input("Enter elements of matrix: "))
        mat.insert(i, ele)
        sum += mat[i]
    print("\nMatrix is:")
    for i in range(0, n):
        print(mat[i], end = " ")
    print()
    print("Sum of maatrix elements: ", sum)
