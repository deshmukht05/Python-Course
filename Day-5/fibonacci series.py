print("Fibonacci Series")
n = int(input("Enter a number: "))
n1=1
n2=2
print(n1)
print(n2)
count=3

while count<=n:
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3
    count+=1
    
