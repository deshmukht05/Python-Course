# 1. abs() : Absolute value of number.

# 2. all() : Returns True if all elements of iterable are True.

# 3. any() : Returns True if any element of the iterable is True.

# 4. ascii() : Returns a string containing printable representation of object.

# 5. bool() : Returns Trure or False

# 6. callable() : Returns True if the object argument appears callable otherwise returns False.

# 7. chr() : Returns string representing character. Argument is Unicode integer.

# 8. complex() : Returns a complex number with given value of real and imaginary.

# 9. dict() : Creates new dictionary

# 10. dir() : Returns the list of names in the current local scope. If argument is given then lists valid attributes for that object.

# 11. divmod() : Returns quotient after division and remainder also for non-complex argument.
# divmod(25, 6)
# (4, 1)

# 12. enumerate() : Returns enumerable object of given iterable, by default starts with 0.
# Example: a="Python"
#          a = enumerate(a, start=10)
#          for i in a:
#             print(i)
# Output:
# (10, 'P')
# (11, 'y')
# (12, 't')
# (13, 'h')
# (14, 'o')
# (15, 'n')

# 13. eval() : Evaluates argument as Python expression.
# a = 12
# eval(a**2//10)
# 14.4

# 14. float() : Returns floating point number from number of string.
# float('1e-004')
# 0.0001
# float(eval('+1.23-13.35'))
# -12.12

# 15. format() : Converts value to formatted representation.

# 16. frozenset() : Returns a new frozenset object.

# 17. globals() : Returns the dictionary representation current global symbol table.

# 18. hash() : Returns hash value of the object. Hash object are integers.

# 19. help() : Returns built-in help system.
# Without argument, starts help utility and changes prompt as-
# help>
# Type quit to exit from help utility.

# 20. hex() : Converts an integer to a lowercase hexadecimal string prefixed with "0x"

# 21. id() : Returns identity of an object. It is unique and constant for each object during its lifetime.

# 22. input() : Inputs value in string.

# 23. int() : Returns integer object constructed from string.

# 24. isinstance() : Returns True if the object argument is an instance of class.
# a = 25
# isinstance(a, int)
# True

# 25. issubclass() : Returns True if given argument is subclass of given class.

# 26. len() : Returns length of an object.

# 27. list() : Returns a list object.

# 28. locals() : Updates and returns a dictionary representing current local symbol table.

# 29. map() : Returns an integer that applies function to every item of iterable, yeilding the result.
# def square(n):
#   return(n*n)
# n = (2, 4, 6, 8)
# result = map(square, n)
# print(list(result))
# [4, 16, 36, 64]

# 30. max() : Returns the largest item in an iterable.

# 31. min() : Returns the smallest item in an iterable.

# 32. oct() : Converts an integer argument to an octal string prefixed with "0o"

# 33. open() : Opens a file and returns a corresponding file object.

# 34. ord() : Returns an integer representing Unicode character.

# 35. pow() : Returns x raised to the power y.

# 36. print() : Print object to the text stream file.

# 37. range() : Generates range of number from start, stop, [step]

# 38. reversed() : Return a reverse iterator.

# 39. round() : Returns rounded to given number of digits precision after decimal point.

# 40. set() : Returns a new set object.

# 41. slice() : Returns a slice object representing the set of indices specified by range.

# 42. sorted() : Returns new sorted list from the items in iterable.

# 43. staticmethod() : Transforms a method into a static method.

# 44. sum() : Returns total of items of an iterable.

# 45. super() : Returns a proxy object that delegates method calls to a parent or sibling class of type.

# 46. tuple() : Returns the tuple object.

# 47. zip() : Makes an iterator thaht aggregates elements from each of the iterable.