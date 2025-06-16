print("Function giving list statistics")
def func(l):
    print("List: ", l)
    print("Total items: ", len(l))
    print("Largest item: ", max(l))
    print("Smallest item: ", min(l))
    l.reverse()
    print("Reverse: ", l)
    l.sort()
    print("Sorted list: ", l)
    
    s = 0
    for i in l:
        s+=i
    print("Sum: ", s)
    return

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
func(list)