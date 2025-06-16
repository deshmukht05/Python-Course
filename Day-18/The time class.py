# The Time Class
# The time class provides time() method ot represent zero time i.e. 0 hours, 0 minutes and 0 seconds

from datetime import time
a = time()
print("Time: ", a)
print()

t1 = time(10, 13, 23)
print("Time: ", t1)
print()

print("Hour: ", t1.hour)
print("Minute: ", t1.minute)
print("Second: ", t1.second)
print("Microsecond: ", t1.microsecond)