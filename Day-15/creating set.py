# We can create set using in-build set() function that can take at the most one argument of any sequence or another iterable object.
print("Creating Set")
t = set("Python Programming")
print(t)

# Type
print("Type: ", type(t))

# Length
print("Length: ", len(t))

# Set
s = ("cat", "dog")
print("Set: ", set(s))

# List to set
l = set(['tushar', 'yash', 'Prajwal'])
print("Set: ", l)

# Add member
l.add('Mayur')
print("Added Mayur: ", l)

# Frozenset
f = frozenset(('tushar', 'yash', 'prajwal'))
print("Frozenset: ", f)