a = int(input("Enter a = "))
b = int(input("Enter b = "))

temp = a
a = b
b = temp

a, b = b, a

a = a+b
b = a-b
a = a-b

print("Value of a = ", a)
print("Value of b = ", b)
