print("Ques. Print the output of following program in tabular format. Also calculate total marks for every element.")
print("Answer: ")
s1 = {'c' : 80, 'c++' : 99, 'Python' : 100, 'NodeJS' : 78}
s2 = {'c' : 89, 'c++' : 87, 'Python' : 80, 'NodeJS' : 98}
s3 = {'c' : 87, 'c++' : 74, 'Python' : 74, 'NodeJS' : 68}
students = {'Tushar' : s1, 'Yash' : s2, 'Prajwal' : s3}
print("Name ", end='\t')
for i in s1.keys():
    print(i.capitalize(), end='\t')
print('Total')
for i in students.keys():
    total = 0
    print(i, end='\t')
    for j in students[i].keys():
        print(students[i][j], end='\t')
        total += students[i][j]
    print(total)