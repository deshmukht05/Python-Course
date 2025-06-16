# Tuple can be created using following ways:
# a. Using pair of parentheses
# b. Using a trailing comma (otherwise it is string)
# c. Separating items with comma
# d. Using tuple()

a = 'b',
print(a)
print()

b=tuple((1, 2, 3, 4))
print(b)
print()

c = tuple()
print("Tuple: ", c)
print()

d = tuple([1, 2, 4, 5])
print("Tuple: ", d)
print()

e = tuple("Tushar")
print("Tuple: ", e)
print()

f = 'mh', 31, 'dk2023'
print("Tuple: ", f)