# Raising exception using raise
a = int(input("Enter a positive number: "))
try: 
    if a<=0:
        raise ValueError("That is zero or negative number.")
except ValueError as error1:
    print(error1)

else:
    print("Yes. This is positive.")
