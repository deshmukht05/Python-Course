# Exception index out of bound
a = [1, 2, 3]
try:
    for ele in range(0, 4):
        print("Element = %d" %(a[ele]))
except IndexError:
    print("An error occured - index out of bound.")