# Nested Dictionary
# This is a dictionary where its item is another dictionary.
# This is unordered collection of dictionary.
# Nested dictionary does not allow slicing.
# It is possible to grow and shrink nested dictionary.
# It also has key and value and accessed using key.

print("Nested Dictionary")
students = {
    1 : {'name' : 'Tushar', 'age' : 23, 'roll_no' : 1},
    2 : {'name' : 'Yash', 'age' : 21, 'roll_no' : 2},
    3 : {'name' : 'Prajwal', 'age' : 23, 'roll_no' : 3}  
}
print("Students:")
print(students)
print()
print("Student 1 details: ")
for k, v in students[1].items():
    print(k.capitalize(), " : ", v)
# print(students[1]['name'])
print()

print("Student 2 details: ")
for i, j in students[2].items():
    print(i.capitalize(), " : ", j)
print()

print("Student 3 details: ")
for l, m in students[3].items():
    print(l.capitalize(), " : ", m)
print()

# Adding a new student 4
print("Student 4 details: ")
students[4] = {}
students[4]['name'] = 'Mayur'
students[4]['age'] = 20
students[4]['roll_no'] = 4
for k, v in students[4].items():
    print(k.capitalize(), " : ", v)
print()

# Delete element of nested dictionary
del students[4]['roll_no']
print("Deleted roll no of student 4:")
for k, v in students[4].items():
    print(k.capitalize(), " : ", v)
print()

# Printing nested dictionary
print("Printing nested dictionary")
print(students)
print()

# Nested for loop is used to print nesred dictionary. Outer loop is for key and inner loop to print values.
for roll, info in students.items():
    print("Serial no: ", roll)
    for k, v in info.items():
        print(k.capitalize(), " : ", v)
    print()