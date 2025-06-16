print("Count vowels in a string")
str = input("Enter a string: ")
l = len(str)
v=0

for a in range(l):
    if str[a] in 'aeiou' or str[a] in 'AEIOU':
        v+=1
print("Vowels in string: ", v)
