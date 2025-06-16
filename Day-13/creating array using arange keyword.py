print("Creating array using arange keyword.")
print("Syntax: <array_name> = numpy.arrange(start, stop, step, dtype)")
print()

import numpy as np
arr = np.arange(10)
print("Array: ", arr)

arr = np.arange(1, 20, 2)
print("Array: ", arr)

arr = np.arange(1.1, 20.1, 2, float)
print("Array: ", arr)
