# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
# 1. "x" - Create - will create a file, returns an error if the file exists
# 2. "a" - Append - will create a file if the specified file does not exists
# 3. "w" - Write - will create a file if the specified file does not exists

f = open("Day-26/demo.txt", "x")
f.write("I am Tushar Deshmukh.")