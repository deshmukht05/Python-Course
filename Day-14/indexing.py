# Tuple index starts from 0.
# For tuple of 10 elements indices are 0 to 9.
# Index is always an integer.
# If attempts to access element outside the tuple then Python will raise IndexError
# Nested tuples are accessed using nested indexing.
t1 = ("Tushar", "Deshmukh", [1, 2, 3], [4, 5, 6], 7, 8, 9)
print(t1)
print("t1[0] & t1[1]: ", t1[0], t1[1])
print("t1[2][2]: ", t1[2][2])