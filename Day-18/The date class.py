# The Date Class:
# The date class in the datetime module contains today() method to represent system date.

from datetime import datetime
from datetime import date
print("The Date Class:")
d = datetime.date(2025, 6, 3)
# d = date(2025, 6, 3)
print("Date: ", d) # TypeError: descriptor 'date' for 'datetime.datetime' objects doesn't apply to a 'int' object 
print()

# Using today() method
e = date.today()
print("Today: ", e)