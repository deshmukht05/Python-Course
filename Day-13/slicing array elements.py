print("Slicing array elements.")
print("1. Slicing array from array index 3 to 5.")
print("2. Slicing array upto 5th element.")
print("3. Slicing array 3rd element onwards.")
print("4. Print all elements.")
print()
from array import *
arr = array("i", [1, 2, 3, 4, 5, 6, 7])
print("Slicing array from array index 3 to 5: ", arr[2:5])

print()
print("Slicing array upto 5th element: ", arr[:5])

print()
print("Slicing array 3rd element onwards: ", arr[3:])

print()
print("All elements: ", arr[:])
