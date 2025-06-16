print("Print number 0 to 11 in array format of different sizes.")
import numpy as np
arr = np.arange(12)
a = arr.reshape(3, 4)
print("Array of 3x4:")
print(a)

print()
c = arr.reshape(4, 3)
print(c)
