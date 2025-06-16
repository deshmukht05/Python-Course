print("Ques. Handle a dictionary of contact name and numbers and provide facilites to add, edit and display contacts.")
print("Answer: ")
d = dict()
while True:
    print("--- Main Menu ---\n"
    "1. Create Contacts\n"
    "2. Edit Contact\n"
    "3. Display Contacts\n")
    o = int(input("Select Main Menu option: "))

    if o==1: #Creating contact
        n = int(input("Enter number of contacts: "))
        for i in range(n):
            key = input("Name: ")
            value = int(input("Enter mobile no.: "))
            d[key] = value
            print()

    elif o==2: #Edit contact list
        print("--- Edit Menu ---\n"
        "1. Add new contact\n"
        "2. Change contact no")
        s = int(input("Select edit menu option: "))
        if s==1:
            key = input("Name: ")
            value = int(input("Enter mobile no.: "))
            d[key] = value
        elif s==2:
            key = input("Enter existing contact name: ")
            value = int(input("Enter new mobile no.: "))
            d[key] = value
        else:
            print("Invalid input.")

    elif o==3: #Display all contacts
        print("Details:")
        for key in d:
            print(key, ':', d[key])
    else:
        print("Invalid input.")

    q = input("Do you wish to continue? (y/n): ")
    if q in 'nN':
        break