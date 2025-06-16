maths = int(input("Enter maths marks: "))
eng = int(input("Enter eng marks: "))
hindi = int(input("Enter hindi marks: "))
sst = int(input("Enter sst marks: "))
science = int(input("Enter science marks: "))
total = maths + eng + hindi + sst + science
percentage = (total/500)*100
print("Total marks obtained: ", total)
print("Percentage: ", percentage)
