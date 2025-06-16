for i in range(4):
    for j in range(i+1):
        print("*", end = " ")
        j+=1
    print()
    i+=1
for i in range(5):
    for j in range(5-i):
        print("*", end = " ")
        j+=1
    print()
    i+=1
