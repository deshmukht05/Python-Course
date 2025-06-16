print("Create 2D list and display it, replace all elements divisible by 10 with zero and print list.")
rno  = int(input("Enter no. of rows: "))
cno = int(input("Enter no. of columns: "))
l = []

for r in range(rno):
    l1 = []
    for c in range(cno):
        print("Enter elements at row", r+1, "columns", c+1, ": ", end = " ")
        element = input()
        l1.append(element)
    l.append(l1)
print("The2D list formed is: ", l)
for r in range(rno):
    for c in range(cno):
        if(int(l[r][c])%10==0):
           l[r][c]='0'
print("The list after updating is: ")
print(l)
