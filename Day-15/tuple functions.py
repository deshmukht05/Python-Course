# len() : Return number of items in the tuple. 
t = (1, 2, 3, 4, 5, 6, 2, 34, 2)
print(t)
print("Length: ", len(t))

# max() : Returns maximum value 
print("Max Value: ", max(t))

# min() : Returns minimum value.
print("Min Value: ", min(t))

# sum() : Returns sum of elements
print("Sum: ", sum(t))

# any() : Returns TRUE if atleast one item in tuple as boolean value TRUE
print("Any: ", any(t))

# all() : Returns TRUE if all items in tuple have any boolean value TRUE.
print("All: ", all(t))

# sorted() : Returns a sorted tuple. 
print("Sorted tuple: ", sorted(t))
print()

# tuple() : Coverts another constructor to tuple. 
st = "Tushar"
print(st)
print("Tuple: ", tuple(st))
print()

# List to tuple 
list = [1, 2, 4, 5, "tushar"]
print("List: ", list)
print("Tuple: ", tuple(list))
print()

# Count
print("Count 2: ", t.count(2))

# Index 
print("Index of 5: ", t.index(5))