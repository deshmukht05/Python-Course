# Menu driven program to sort list using bubble sort, insertion sort and selection sort
def bubble(l):
    print()
    print("Bubble Sort")
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if(l[j]>l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
    print("List after sorting: ", l)

def insertion(l):
    print()
    print("Insertion Sort")
    for i in range(1, len(l)):
        key = l[i]
        j = i-1
        while j>0 and key < l[j]:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    print("List after sorting: ", l)

def selection(l):
    print()
    print("Selection Sort")
    i = 0
    while i<len(l):
        smallest = min(l[i:])
        ind = l.index(smallest)
        # Swapping
        l[i], l[ind] = l[ind], l[i]
        i+=1
    print(l)

print("1. Bubble Sort\n"
      "2. Selection Sort\n" \
      "3. Insertion Sort")

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        l = eval(input("Enter a list: "))
        n = list(l)
        bubble(n)
    
    elif choice == 2:
        l = eval(input("Enter a list: "))
        n = list(l)
        selection(n)

    elif choice == 3:
        l = eval(input("Enter a list: "))
        n = list(l)
        insertion(n)
    else:
        print("Invalid input.")
        a = input("Do you want to continue(y/n): ")
        if a in 'NONono':
            break
        