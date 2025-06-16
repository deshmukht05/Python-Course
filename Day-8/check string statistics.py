print("Checking string statistics(Upper Case, Lower Case, Digits, Spaces and Delimiters or Printable)")
str = input("Enter a string: ")
u=l=d=p=s=0

for a in str:
    if a.isupper():
        u+=1
    elif a.islower():
        l+=1
    elif a.isdigit():
        d+=1
    elif a.isspace():
        p+=1
    elif a.isprintable():
        s+=1
    else:
        exit

print("Statistics is:")
print("Upper case: ", u)
print("Lower case: ", l)
print("Digits: ", d)
print("Spaces: ", p)
print("Delimiters: ", s)
