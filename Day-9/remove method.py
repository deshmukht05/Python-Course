print("Remove Method")
print("Removes first occurance of member from the list that has value of x.")
print()
str = ["Tushar", "Yash", "Prajwal"]
print("Original list: ", str)
str.remove("Tushar")
print("New list: ", str)

print()

rm = input("Enter name to remove: ")
str.remove(rm.capitalize())
print("New list", str)
