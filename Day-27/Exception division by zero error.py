# Exception division by zero error
def divide(divisor):
    for ele in divisor:
        try:
            print("36/", ele, end=" = ")
            print(36/ele)
        except(ZeroDivisionError):
            print("Error - Diviosn by Zero")
        except(TypeError):
            print("Error-non numberic divisor")

divisor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'T']        
divide(divisor)

print()
print()

def divide():
    for ele in range(1, 11):
        try:
            print("36 x ", ele, end=" = ")
            print(36 * ele)
        except(ZeroDivisionError):
            print("Error - Diviosn by Zero")
        except(TypeError):
            print("Error-non numberic divisor")
            
divide()