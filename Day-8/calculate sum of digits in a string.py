print("Calculate sum of digits in a string.")
#Enter numbers as a string
#For sentence or characters it will give 0 output 
str = input("Enter a string: ")
s=0

for char in str:
    if char.isdigit():
        s+=int(char)
print("Sum of digits: ", s)
