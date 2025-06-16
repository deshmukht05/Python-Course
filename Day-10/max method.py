print("Max Method")
print("Returns the lagest member in an iterable or largest of two or more arguments.")
print("If more than one member shares the maximum value then it returns first occurence.")
print()
n1=[23, 34, 23, 22, 43, 34, 92]
print("String: ", n1)
print("Max value: ", max(n1))

print()

fruits = ["Apple", "Mango", "Banana"]
print("Fruits: ", fruits)
print("Max value: ", max(fruits))

print()

fruits = ["Apple", "Mango", "banana"]
print("Fruits: ", fruits)
print("Max value: ", max(fruits))  #It goes with ASCII values and will print banana bcoz there is small 'b' and small letters appears first in ASCII values

print()

num = [[1, 2, 4, 8], [3, 2, 2, 3]]
print("Numbers: ", num)
print("Max value: ", max(num))

print()

num = [[8, 2, 4, 8], [3, 2, 2, 3]]
print("Numbers: ", num)
print("Max value: ", max(num))
