num1 = 100
num2 = 999

for n in range(num1, num2+1):
    temp = n
    sum = 0
    while temp>0:
        digit = temp%10
        sum += digit**3
        temp//=10
    if n==sum:
        print(n)

n = int(input("Enter a number: "))
if n>0:
    sum=0
    digit = n%10
    sum += digit**3
    n//=10
    print("An armstrong number.")

else:
    print("Not an armstrong number.")
