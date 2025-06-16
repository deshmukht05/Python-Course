n = input("Enter any single thing from keyboard: ")
if (n >= "A") and (n <= "Z"):
    print(n, " is in Uppercase")
    
elif (n >= "a") and (n <= "z"):
    print(n, " is in Lowercase")

elif n>="0" and n<="9":
    print(n, "is a number.")
    
else:
    print(n, " is a special character.")
