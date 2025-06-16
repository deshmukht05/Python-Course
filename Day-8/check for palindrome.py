print("Checking whether given string is Palindrome or not.")
str = input("Enter a string: ")
l = len(str)
mid = int(l/2)
b=-1

for f in range(mid):
    if str[f]==str[b]:
        f+=1
        b-=1
    else:
        print(str, " is not a Palindrome.")
        break

else:
    print(str, " is Paindrome.")
