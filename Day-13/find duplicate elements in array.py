print("Find duplicate elements in array.")
from array import *
arr1 = array("i", [1, 2, 3, 4, 5, 5, 5, 3])
print("Array: ", arr1)

s = set()
duplicate = set()
flag = 0

for i in range(len(arr1)):
    if arr1[i] in s:
        if arr1[i] not in duplicate:
            print("Duplicate values: ", arr1[i])
            flag=1
            duplicate.add(arr1[i])
    else:
        s.add(arr1[i])
if flag==0:
    print("No duplicates found.")
