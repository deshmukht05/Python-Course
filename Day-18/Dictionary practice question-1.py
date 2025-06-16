print("Ques. Store marks of 3 students in 4 subjects in separate dictionaries. Create a nested dictionary that stores name and makrs, details from previously dreated dictionaries and print.")
print("Answer: ")
s1 = {'c' : 80, 'c++' : 99, 'Python' : 100, 'NodeJS' : 78}
s2 = {'c' : 89, 'c++' : 87, 'Python' : 80, 'NodeJS' : 98}
s3 = {'c' : 87, 'c++' : 74, 'Python' : 74, 'NodeJS' : 68}
students = {'Tushar' : s1, 'Yash' : s2, 'Prajwal' : s3}
for i in students.keys():
    print("Name: ", i)
    print("Subject \tMarks")
    for j in students[i].keys():
        print(j, "\t\t", students[i][j])
    print()