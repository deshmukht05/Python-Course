print("SPLITLINES Method")
print()
str = "123\n456\n789\n"
print(str.splitlines())

print()
str = "123\n\n456\n789\n\n"
print(str.splitlines())

print()
str = "123\n\n456\n789\n\n"
print(str.splitlines(keepends=True))
