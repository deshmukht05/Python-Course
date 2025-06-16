print("Using while loop.")
r=1
while r<=5:
    c=1
    while c<=r:
        print("*", end = " ")
        c+=1
    print()
    r+=1

print()
print()

print("Using for loop.")
#r=1
for i in range(5):
    for j in range(i+1):
        print("*", end = " ")
        j+=1
    print()
    i+=1
print()
