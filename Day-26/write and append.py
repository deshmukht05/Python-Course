# Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:
# 1. "a" - Append - will append to the end of the file
# 2. "w" - Write - will overwrite any existing content

with open("Day-26/sample.txt", "a") as f:
    f.write(" Now a days I am getting boring.")

with open("Day-26/sample.txt") as f:
    print(f.read())

print()
print()

with open("Day-26/sample.txt", "w") as f:
    f.write("I am Tushar Deshmukh.")

with open("Day-26/sample.txt") as f:
    print(f.read())