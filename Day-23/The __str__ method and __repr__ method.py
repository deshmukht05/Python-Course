# The __str__ method and __repr__ method:
# - These are special method that returns representation of an object. 
# - The __str__ method is useful for string representation of object. this is called when str() or print() function is invoked on the object. 
# - The __repr__ method returns object representation. It may be any valid Python expression like tuple, dictionary, string, etc. This is called when repr() function is invoked on the object. 
# - The __str__ method is in most human-readable format and __repr__ method is meant for developers and for debuggers than actually using in module.