# Accessing instance members
class student:
    roll = 1
    name = "Rohit"
    marks = 98

    def display(self):
        print("Name: ", str(self.name))
        print("Roll No.: ", str(self.roll))
        print("Marks: ", str(self.marks))

s1 = student()
s1.display()