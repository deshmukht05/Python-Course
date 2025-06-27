# Divison using try except else
a = int(input("Enter a number to divide: "))
b = int(input("Enter a number to divide by: "))

try:
    c = a/b
except ZeroDivisionError:
    print("Exception - Divide by zero")
else:
    print(a, "/", b, "=", c)