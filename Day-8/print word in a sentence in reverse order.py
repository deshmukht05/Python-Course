print("Program to print word in a sentence in reverse order")
str = input("Enter a string: ")
print()
word = str.split()
words = word[::-1]
rev_sentence = ' '.join(words)
print("Using slice:")
print("Reversed string: ", rev_sentence)

print()
word = str.split()
rev_sent = ' '.join(reversed(word))
print("Using reversed() keyword:")
print("Reversed string: ", rev_sent)
