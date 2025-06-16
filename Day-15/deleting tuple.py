# Python does not allow to delete individual elements of tuple or allows to delete tuple entirely.
# The keyword del is used to delete tuple.
tup = (1, 2, 3, [4, 5])
print("Original: ", tup)
# del tup[3][0]
del tup
print(tup)