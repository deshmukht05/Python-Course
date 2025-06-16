maths = int(input("Enter maths marks: "))
eng = int(input("Enter english marks: "))
hindi = int(input("Enter hindi marks: "))
sst = int(input("Enter sst marks: "))
science = int(input("Enter science marks: "))
    
total = maths + eng + hindi + sst + science
per = (total/500)*100
print("Total marks: ", total)
print("Percentage: ", per)

if per>90 and  per<=100:
    print("Grade: A+ Pass")
elif per<=90 and per>85:
    print("Grade: A Pass")
elif per<=85 and per>70:
    print("Grade: B Pass")
elif per<=70 and per>50:
    print("Grade: C Pass")
elif per<=50 and per>=35:
    print("Grade: D Pass")
else:
    print("Failed in exam")
