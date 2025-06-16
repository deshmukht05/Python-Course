print("Print alternate characters in upper case.")
str1 = input("Enter a string: ")

print("Original String: ", str1)
l = len(str1)
str2 = " "

for a in range(0, l, 2):
    str2 += str1[a]
    if a<(l-1):
        str2 += str1[a+1].upper()
print("Alternate character uppercase: ", str2)