p = int(input("Enter principle: "))
t = int(input("Enter duration in year: "))
r = int(input("Enter rate: "))

si = (p*t*r)/100
total = si + p

print("Simple interest: ", si)
print("Total amount: ", total)
