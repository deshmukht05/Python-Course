# Accessing dictionary elements
stud = {"name" : "Tushar", "roll_no" : 12, "total_marks" : 500}
print(stud)
a = stud["name"]
b = stud["roll_no"]
c = stud["total_marks"]
print(a, b, c)
print()

# Printing Dictionary
# 1. Printing keys only
print("Keys: ")
for i in stud.keys():
    print(i)
print()

# 2. Printing values only
print("Values: ")
for i in stud.values():
    print(i)
print()

# 3. Printing keys and values
print("Keys and Values: ")
for i, j in stud.items():
    print(i, " : ", j)
print()

# 4. Printing multiple items
marks = {"Tushar" : 100, "Yash" : 90, "Prajwal" : 80}
for i, j in marks.items():
    print("%s scored %d" %(i, j))
print()

# 5. Printing multiple of 2
print("Table of 2: ")
double = {x : 2 * x for x in range(11)}
print(double)
print()

print("Table of 2:")
for i, j in double.items():
    print("2 x %d : %d" %(i, j))