print("Calculate sum of tuple items using function.")
def sum(m):
    s = 0
    for i in m:
        s+=i
        i+=1
    return s

n = (1, 2, 3, 4, 5)
print("Sum: ", sum(n))