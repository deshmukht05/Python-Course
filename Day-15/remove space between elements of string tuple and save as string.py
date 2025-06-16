print("Remove space between elements of string tuple and save as string")
x = (1, 2, 3, 'a b c ', 5)
print("Original tuple: ", x)

y = str(x).replace(' ', '')
print("Tuple after removing space: ", str(y))