def display():
    print("Square and Cude using function.")

def square(m):
    # sq = m**2
    # print("Square: ", sq)
    return m**2

def cube(m):
    # cu = m**3
    # print("Cude: ", cu)
    return m**3

display()
n = int(input("Enter a number: "))
# square(n)
# cube(n)
print("Square: ", square(n))
print("Cude: ", cube(n))