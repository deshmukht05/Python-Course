print("Program to sort names.")
str = input("Enter names: ")
name_list = str.split()
name_list.sort()

print("Sorted names are:")
for name in name_list:
    print(name)
