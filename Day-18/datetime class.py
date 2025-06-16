# The datetime class
# This class contains information about date and time both.
# In the constructor datetime class, year, month and day number is mandatory.

print("The datetime Class")
from datetime import datetime
print("Date: ", datetime(2025, 6, 3, 12, 23, 32, 23000))
print()

t1 = datetime(2025, 6, 3, 12, 23, 32, 23000)
print("Year: ", t1.year)
print("Month: ", t1.month)
print("Day: ", t1.day)
print("Hours: ", t1.hour)
print("Minute: ", t1.minute)
print("Second: ", t1.second)
print("Microsecond: ", t1.microsecond)
print("Timestamp: ", t1.timestamp())