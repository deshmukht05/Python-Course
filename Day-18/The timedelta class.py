# The timedelta class
# The object of timedelta class is used to represent difference between two dates or two times.

from datetime import date, timedelta
t1 = date(year = 2010, month = 5, day = 10)
t2 = date(year = 2020, month = 12, day = 30)
print("t1 = ", t1, "\nt2 = ", t2)
t3 = t1-t2
print("Difference: ", t3)
print()

t4 = timedelta(days=10, seconds=40)
t5 = timedelta(days=4, minutes=20, seconds=30)
print("t4: ", t4, "\nt5: ", t5)
t6 = t4-t5
print("Difference: ", t6)
print("Total seconds: ", t6.total_seconds())
print()

# The total_seconds() method is used to find total seconds of given date & time.
t7 = timedelta(minutes=10)
print("t7: ", t7)
print("Seconds: ", t7.total_seconds())