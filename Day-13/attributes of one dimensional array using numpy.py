print("Attributes of one dimensional array using numpy.")
import numpy as np
l = [1, 2, 3, 4, 5, 6]
arr = np.array(l)
print("Array is: ", arr)
print("Type of array: ", type(arr))
print("Dimensions: ", arr.shape)
print("Element size: ", arr.size)
print("Element itemsize: ", arr.itemsize, "bytes")
print("Data type: ", arr.dtype)
