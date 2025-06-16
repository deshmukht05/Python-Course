print("Create list using cartesian product of 2 lists")
l = [x+y for x in ['a', 'b', 'c'] for y in ['x', 'y', 'z']]
print(l)
