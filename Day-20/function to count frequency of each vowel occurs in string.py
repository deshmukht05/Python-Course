print("Function to count frequency of each vowel occurs in string.")
def vowels(s):
    vowels = 'aeiou'
    count = {}.fromkeys(vowels, 0)
    for char in s:
        if char in count:
            count[char] += 1
    for v, c in count.items():
        print(v, c)

s = input("Enter a string: ")
s = s.casefold()
vowels(s)