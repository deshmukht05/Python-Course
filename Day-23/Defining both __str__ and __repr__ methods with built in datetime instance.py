# Defining both __str__ and __repr__ methods with built in datetime instance
import datetime
d = datetime.datetime.now()
print(d)
print(repr(d))
print(str(d))