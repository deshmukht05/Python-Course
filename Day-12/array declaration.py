from array import *
arr = array("i", [1, 23, 2,34])
print("Array: ", arr)
print("Type of array: ", type(arr))
print("Type of value: ", type(arr[0]))

print("Integer values:")
for i in arr:
    print(i, end = " ")

print()
print()
arr1 = array("f", [1.2, 1.5, 2.4])
print("Array: ", arr1)
print("Type of array: ", type(arr1))
print("Type of values: ", type(arr[1]))

print("Float values:")
for i in arr1:
    print(i, end= " ")

print()
print()
print("Integer values from 0 to 7")
arr2 = array("i", range(8))
print(arr2)
