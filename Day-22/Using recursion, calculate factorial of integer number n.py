# Using recursion, calculate factorial of integer number n
def factorial(m):
    if m==1:
        return 1
    else:
        return (m*factorial(m-1))

n = int(input("Enter a number: "))
print("Factorial: ", factorial(n))