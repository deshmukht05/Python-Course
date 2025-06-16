# We know that tuple is immutable i.e. its elements cannot be changed
# But if list is an element of any tuple, its items can be changed as list is mutable.
tup = (1, 2, 3, [4, 5])
print("Original", tup)
# tup[0]=0
tup[3][0] = 0
print(tup)