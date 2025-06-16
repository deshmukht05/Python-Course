# Empty dictionary
dict1 = {}
print("Empty dictionary: ", dict1)
print("Type of empty dictionary: ", type(dict1))
print()

# Dictionary with integer key
n = {"name" : "Tushar", "roll_no" : 123, "class" : "10th B"}
print(n)
print(n["roll_no"])
print()

# Dictionary with mixed key
m = {"name" : "Tushar", "marks" : [12, 23, 42, 23]}
print(m)
print(m["marks"])
print(m["marks"][1])
print()

# Dictionary with tuple as key
d = {(1, 2, 3, 4, 5) : "abcde"}
print(d)
print(d[(1, 2, 3, 4, 5)])
print()

# Dictionary using "for"
cude = {x : x*x*x for x in range(11)}
print(cude)
print()

# Dictionary using "for" with criteria
squ = {x : 2*x for x in range(11) if x%2==0}
print(squ)