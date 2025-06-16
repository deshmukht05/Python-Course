# To create and edit mobile dictionary
def create(d):
    n = int(input("Enter number of contacts: "))
    for i in range(n):
        key = input("Enter name: ")
        value = int(input("Enter mobile no.: "))
        d[key] = value

def edit(d):
    print("--- Edit Menu ---\n" \
    "1. Add a new contact\n" \
    "2. Change contact number")
    n = int(input("Select option: "))

    if n==1:
        key = input("Enter name: ")
        value = int(input("Enter mobile number: "))
        d[key] = value
    elif n==2:
        key = input("Enter existing name: ")
        value = int(input("ENter new mobile number: "))
        d[key] = value
    else:
        print("Invalid input.")
        n = input("Want to continue(y/n): ")
        if n in 'YesyesYES':
            edit()

def display(d):
    for key in d:
        print("Name: ", key, "\tMobile no.:", d[key])

print("--- Main Menu ---\n" \
"1. Create Dictionary\n" \
"2. Edit Dictionary\n" \
"3. Display Dictionary")

d=dict()

while True:
    n = int(input("Enter your choice: "))

    if n==1:
        create(d)
    elif n==2:
        edit(d)
    elif n==3:
        display(d)
    else:
        print("Invalid input.")
    
    m = input("Want to continue(y/n): ")
    if m in 'NoNOno':
        break