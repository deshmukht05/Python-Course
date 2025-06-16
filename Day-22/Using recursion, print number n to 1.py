# Using recursion, print number n to 1
def print_reverse(m):
    if m<=0:
        pass
    else:
        print(m, end=' ')
        print_reverse(m-1)

n = int(input("Enter a number: "))
print_reverse(n)