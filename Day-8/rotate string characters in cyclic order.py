print("Rotate string characters in cyclic order.")
str = input("Enter a word: ")
for i in range(len(str)):
    print(str[i:], end = "")
    print(str[0:i])

#Another method
print()
for i in range(len(str)):
    word = str[i:] + str[:i]  #Added both
    print(word)
