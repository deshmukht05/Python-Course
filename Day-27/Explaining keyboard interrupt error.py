# Explaining keyboard interrupt error
try:
    for ele in range(0, 3):
        print("Enter a number: ^c to interrupt")
        n = input()
        print(n)
except KeyboardInterrupt:
    print("Caught KeyboardInterrupt - Crtl + C pressed")

else:
    print("No exception raised.")