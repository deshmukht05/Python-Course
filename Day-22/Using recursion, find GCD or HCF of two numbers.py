# Using recursion, find GCD/HCF of two numbers
def gdc(m, n):
    if n==0:
        return m
    else:
        return gdc(n, m%n)

n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))
print("GCD: ", gdc(n1, n2))