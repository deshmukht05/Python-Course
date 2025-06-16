print("Functions to create list, send to another function to convert to array and calculate sum of array elements.")

from array import *

def create_list():
    n = int(input("Enter the size of list: "))
    global l
    l = []
    for i in range(0, n):
        item = int(input("Enter element: "))
        l.insert(i, item)

def list_to_array():
    ar = array("i", l)
    print("Array: ")
    s = 0
    for i in ar:
        print(i, end=" ")
        s+=i
    print("\nSum: ", s)

create_list()
list_to_array()