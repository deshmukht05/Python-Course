print("Find age of a person")
# Method-1
from datetime import date, datetime
t1 = date(year=2002, month=2, day=5)
t2 = date(year=2025, month=6, day=4)
t3 = (t2.year)-(t1.year)
print("Your age: ", t3)
print()

# Method-2
dob_string = input("Enter date of birth in dd-mm-yyyy format: ")
dob_object = datetime.strptime(dob_string, "%d-%m-%Y")
today = datetime.now()
diff = today.year - dob_object.year
print("Your age: ", diff)