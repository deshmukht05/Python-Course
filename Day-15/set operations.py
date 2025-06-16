print("Set Operations")
a = {'a', 'b', 'c', 'd', 1, 2, 3, 4}
b = {'c', 2, 3, 'p', 'f', 'x'}
print("a: ", a)
print("b: ", b)
print()

#Difference
print("Difference of a in b: ", a.difference(b))
print("Difference of b in a: ", b.difference(a))
print()

# Union
print("Union of a and b: ", a.union(b))
print("Union of b and a: ", b|a)
print()

# Intersection
print("Intersection of a and b: ", a.intersection(b))
print("Intersection a-b: ", a-b)
print("Intersection b-a: ", b-a)

# Pop
print("After Pop from a: ", a.pop())
print("After Pop from b: ", b.pop())