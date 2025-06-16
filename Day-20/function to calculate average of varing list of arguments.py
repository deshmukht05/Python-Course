print("Function to calculate average of varing list of arguments (i.e. arbitary number of parameters.)")
# In many situations, programmers may not know exact number of values to be processed.
# In Python, asterisk is used to represent reference to tuple consists of any number of items. (Do not compare asterisk with C pointers)
# In python, asterisk is used in front of last parameter name to denote it as a tuple reference.

def am(first, *values):
    """Calculate arithmetic mean"""
    print("First: ", first)
    s = sum(values)
    print("Sum: ", s)
    return (first + s) / (1 + len(values))

print(am(1, 2, 3, 4, 5))
print(am(6, 7, 8, 9, 10, 12, 13, 14, 15))
print(am(3, 2, 1, 5, 6, 5, 3, 7, 2))