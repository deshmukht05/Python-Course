import numpy as np
print("Product of 2 arrays.")
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = a*b
print("Using * operator:")
print(c)

print()
e = np.array([[1, 2, 3], [4, 5, 6]])
f = np.array([[1, 2], [3, 4], [5, 6]])
print("Using dot() method: ")
d = e.dot(f)
print(d)