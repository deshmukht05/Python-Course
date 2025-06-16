print("Insert Method")
print("Syntax: insert(i, x)")
print("Inserts item x at position i")
n = ["Tushar", 0, 2, "Yash", 4, 3]
n.insert(6, "Prajwal")
n.insert(7, 6)
n.insert(8, 5)
print("New list: ", n)

print()

str = input("Enter a number or word: ")
posi = int(input("Enter position: "))
n.insert(posi, str)
print(n)
