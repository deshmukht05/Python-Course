print("Initialize and print array, also calculate sum of elements.")
from array import *
arr1 = array("i", [1, 2, 3, 4, 5])
print("Array: ", arr1)

sum = 0
for i in range(len(arr1)):
    sum+=i
print("Sum: ", sum)
