# To perform queue operations on list
def insert(qu, item):
    qu.append(item)
    if len(qu)==1:
        front=rear=0
    else:
        rear=len(qu)-1

def isempty(qu):
    if qu==[]:
        return True
    else:
        return False

def delete(qu):
    if isempty(qu):
        return "underflow"
    else:
        item = qu[0]
        qu.remove(item)
        if len(qu)==0:
            front = None
        else:
            front = qu[0]
    return item

def display(qu):
    if isempty(qu):
        print("Queue is empty.")
    elif len(qu) == 1:
        print(qu[0], "<==front, rear.")
    else:
        front = 0
        rear = len(qu)-1
        print(qu[front], "<--front")

        for a in range(1, rear):
            print(qu[a])
        print(qu[rear], "<--rear")

qu = []
front = None
print("Queue Operations")
print("1. Insert\n"
    "2. Delete\n"
    "3. Display")

while True:
    ch = int(input("Enter your choice: "))
    if ch==1:
        item = int(input("Enter item: "))
        insert(qu, item)
    
    elif ch==2:
        item = delete(qu)
        if item=="underflow":
            print("Underflow! Queue is empty.")
        else:
            print("Deleted: ", item)
    
    elif ch==3:
        display(qu)
    
    a = input("Do you want to continue(y/n): ")
    if a in "YESYesyes":
        continue
    else:
        break