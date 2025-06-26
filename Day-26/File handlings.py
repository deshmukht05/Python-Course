# File Handling:
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# 1. "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# 2. "a" - Append - Opens a file for appending, creates the file if it does not exist
# 3. "w" - Write - Opens a file for writing, creates the file if it does not exist
# 4. "x" - Create - Creates the specified file, returns an error if the file exists

with open("Day-26/sample.txt") as f:
    print(f.read())

print()
print()

f = open("Day-26/sample.txt")
print(f.readline())
f.close()

print()
print()

f = open("Day-26/sample.txt")
print(f.readlines())
f.close()

print()
print()

f = open("Day-26/sample.txt")
print(f.read(5))
f.close()

print()
print()

with open("Day-26/sample.txt") as f:
    for x in f:
        print(x, end = "")