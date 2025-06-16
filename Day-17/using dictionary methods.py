print("Using dictionary methods")
keys = {'a', 'e', 'i', 'o', 'u'}
vowels = dict.fromkeys(keys)
print(vowels)
print()

# Assign value
vowels = "Vowel"
v = dict.fromkeys(keys, vowels)
print(v)
print()

# Sorting
print(sorted(keys))