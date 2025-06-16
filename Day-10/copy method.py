print("Copy Method")
print("Returs a copy of list.")
print()
list = [1, 23, 34, 4]
print("List 1: ", list)
list2 = list.copy()
print("List 2: ", list2)
list.append(5)
print("After append list 1: ", list) #Only List 1 changed
print("After append List 2: ", list2)  #List 2 will not have any changes
