print("Interchange alternta elements in list.")
l = eval(input("Enter matrix A: "))
n = list(l)
for i in range(0, len(n)-1, 2):
    j=i+1
    n[i], n[j] = n[j], n[i]

print()
print("Updated list:")
print(n)
