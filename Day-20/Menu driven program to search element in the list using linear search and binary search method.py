# Menu driven program to search element in the list using linear search and binary search method.
def linear_search(l, item):
    i = 0
    while i<len(l):
        if l[i]==item:
            print(item, " found at position ", i+1)
            break
        i+1
    else:
        print(item, " not found in list.")

def binary_search(l, item):
    beg = 0
    last = 0
    while beg<=last:
        mid = (beg+last)//2
        if item == l[mid]:
            print(item, " found at position, ", mid+1)
            break
        elif item > l[mid]:
            beg = mid+1
        else:
            last = mid-1
    else:
        print(item, " not found.")

print("--- Options ---\n" \
"1. Linear Search\n" \
"2. Binary Search")
print()

while True:
    op = int(input("Select any option: "))
    if op==1:
        print()
        print("Linear Search")
        l = eval(input("Enter a list: "))
        n = list(l)
        ele = int(input("Enter a number to search: "))
        linear_search(n, ele)
    
    elif op==2:
        print()
        print("Binary Search")
        l = eval(input("Enter a sorted list: "))
        n = list(l)
        ele = int(input("Enter a number to search: "))
        binary_search(n, ele)
    else:
        break