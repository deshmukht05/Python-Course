b = int(input("Enter base number: "))
p = int(input("Enter the power: "))
i = 1

fact=1
print(f"Factorial of {b} number")
while i<=b:
    fact = fact*i
    i+=1
print("Factorial: ", fact)
print()


i = 1
result=1
while i<=p:
    result = result*b
    i+=1

print("Result: ",result)
print()

s=0
i=1
print("Addition of number")
while b<=result:
    print(b, end = " ")
    s = s + b
    b = b+1

print()
print("Addition: ", s)
