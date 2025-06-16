# Using recursion, generate n terms of fibonacci series
def fibonacci(m):
    if m<=1:
        return m
    else:
        return (fibonacci(m-1) + fibonacci(m-2))

terms = int(input("Enter a number: "))

for i in range(1, terms+1):
    print(fibonacci(i), end=' ')