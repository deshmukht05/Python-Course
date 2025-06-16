# Menu driven program to call functions for 
# 1. Interchange first half elements with second half of a list 
# 2. Count and sum even elements of the list of numbers.
# 3. Count and sun odd elements of the list of numbers.

def swap_half(list):
    length = len(list)
    if length%2==0:
        mid = length//2
        print("Mid: ", mid)
        for i in range(mid):
            list[i], list[mid+i] = list[mid+i], list[i]
        print("After interchanging: ", list)
    else:
        print("Can not half the list.")

def even_num(list):
    c=s=0
    for i in list:
        if i%2==0:
            c+=1
            s+=i
    print("Count of even numbers: ", c)
    print("Sum of even numbers: ", s)

def odd_num(list):
    c=s=0
    for i in list:
        if i%2!=0:
            c+=1
            s+=i
    print("Count of odd numbers: ", c)
    print("Sum of odd numbers: ", s)

print("--- Options ---\n" \
"1. Interchange list from half\n" \
"2. Count and Sum of even numbers\n" \
"3. Count and Sum of odd numbers")
print()
l = int(input("Select one option: "))

while(l in(1, 2, 3)):
    li = eval(input("Enter list: "))
    n = list(li)
    if l==1:
        swap_half(n)
    
    elif l==2:
        even_num(n)

    elif l==3:
        odd_num(n)
    
    l = int(input("Select any option or any other number to exit: "))