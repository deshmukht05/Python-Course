# Once tuple is created, it does not allow to add new element, but we can reassign a tuple.
tup = (1, 2, 3, [4, 5])
# tup[4] = "cat"
# tup[3][2] = 3
tup = (1, 2, 3, [4, 5], "cat")
print(tup)