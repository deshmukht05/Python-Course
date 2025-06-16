for i in range(5):
    for j in range(5-i):
        print("*", end = " ")
        j+=1
    print()
    i+=1

print()
print()

r=6
while r>=1:
    c=1
    while c<=r-1:
        print("*", end = " ")
        c+=1
    print()
    r-=1
