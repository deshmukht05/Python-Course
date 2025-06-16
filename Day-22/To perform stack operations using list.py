# To perform stack operations using list
def isempty(stk):
    if stk==[]:
        return True
    return False

def pop(stk):
    item = stk.pop()
    if len(stk)==0:
        top = None
    else:
        top = len(stk)-1
    return item

def push(stk, item):
    stk.append(item)
    top = len(stk)-1

def peep(stk):
    if isempty(stk):
        return "underflow"
    else:
        top = len(stk)-1
        return stk[top]

def display(stk):
    if isempty(stk):
        print("Stack empty.")
    else:
        top = len(stk)-1
        print(stk[top], '<-top')
        for a in range(top-1, -1, -1):
            print(stk[a])

Stack = []
top = None
print("Stack Operations")
print("1. Push\n" \
"2. Peep\n" \
"3. Pop\n" \
"4. Display\n" \
"5. Exit")

while True:
    n = int(input("Select option: "))
    if n==1:
        item = int(input("Enter value: "))
        push(Stack, item)
    
    elif n==2:
        item=peep(Stack)
        if item=='underflow':
            print("Underflow! Stack is empty.")
        else:
            print("Top os the Stack is ", item)
    
    elif n==3:
        item=pop(Stack)
        if item=='underflow':
            print("Underflow!, Stack is empty.")
        else:
            print("Popped item is: ", item)
    
    elif n==4:
        display(Stack)
    
    elif n==5:
        break

    else:
        print("Invalid input.")
    print()