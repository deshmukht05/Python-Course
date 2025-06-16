print("Small Letters")
ch = 97
while ch<=122:
    print(chr(ch), end = " ")
    ch+=1
    
print()
print()
print("Capital Letters")
ch = 65
while ch<=90:
    print(chr(ch), end = " ")
    ch+=1


print()
print()
print("All ASCI Values")
ch=1
while ch<=256:
    print(ch, end = "-")
    print(chr(ch), end = ", ")
    ch+=1
