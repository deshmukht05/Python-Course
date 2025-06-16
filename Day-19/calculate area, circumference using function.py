print("Calculate area, circumference using function.")
def selection(m):
    match m:
        case 1:
            # Radius of circle
            r = int(input("Enter radius: "))
            area = 3.14 * r * r
            print("Area of circle: ", area)
        
        case 2:
            # Circumference of circle
            r = int(input("Enter radius: "))
            cir = 2 * 3.14 * r
            print("Circumference of circle: ", cir)

print("--- Options ---\n"
      "1. Area of circle\n"
      "2. Circumference of circle")

n = int(input("Select option: "))

# Check if number is less then equal to 2
if n<=2:
    selection(n)
else:
    print("Invalid input value.")