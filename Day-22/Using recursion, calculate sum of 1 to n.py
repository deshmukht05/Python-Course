# Using recursion, calculate sum of 1 to n
def sum(m):
    if m==1:
        return 1
    else:
        return (m + sum(m-1))

n = int(input("Enter a number: "))
print("Sum of 1 to", n ,": ", sum(n))