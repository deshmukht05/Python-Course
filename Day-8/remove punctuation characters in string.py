print("Program to remove punctuation in a string.")
str = input("Enter a string: ")
punctuations = '''~`!@#$%^&*()_+-=:";'<>,./?|\[]{}'''
str1 = " "
ch = "a to z" and "A to Z"

for ch in str:
    if ch not in punctuations:
        str1 += ch
print("After removing punctuations: ", str1)
