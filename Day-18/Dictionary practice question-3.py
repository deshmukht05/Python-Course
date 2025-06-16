print("Ques. Declare 3 dictionaries containing name and marks in 4 subjects, as member of list and print details.")
print("Answer: ")
stud = [{'Name' : 'Tushar', 's1' : 90, 's2' : 98, 's3' : 97 , 's4' : 100},
        {'Name' : 'Yash', 's1' : 92, 's2' : 89, 's3' : 79 , 's4' : 86},
        {'Name' : 'Prajwal', 's1' : 93, 's2' : 94, 's3' : 96 , 's4' : 97}
]
for i in stud[0]:
    print(i, end='\t')  #Printing headings
print()
for i in range(len(stud)):
    s = stud[i]
    for j in s.values():
        print(j, end='\t')
    print()