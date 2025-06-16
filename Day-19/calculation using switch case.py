print("Calculation using switch case.")
def selection(m):
    match m:
        case 1:
            n1 = int(input("Enter 1st number: "))
            n2 = int(input("Enter 2nd number: "))
            sum = n1+n2
            print("Sum: ", sum)
        case 2:
            n1 = int(input("Enter 1st number: "))
            n2 = int(input("Enter 2nd number: "))
            sub = n1-n2
            print("Subtraction: ", sub)
        case 3:
            n1 = int(input("Enter 1st number: "))
            n2 = int(input("Enter 2nd number: "))
            mul = n1*n2
            print("Multiplication: ", mul)
        case 4:
            n1 = int(input("Enter 1st number: "))
            n2 = int(input("Enter 2nd number: "))
            div = n1/n2
            print("Division: ", div)

print("--- Options ---\n"
      "1. Sum\n"
      "2. Subtract\n"
      "3. Multiplication\n"
      "4. Division")

n = int(input("Select option: "))

# Check if number is less then equal to 4
if n<=4:
    selection(n)
else:
    print("Invalid input value.")