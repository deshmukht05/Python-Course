# Use of __init__ constructor
class student:
    def __init__(self, n, r, m):
        self.name = "Akshay"
        self.roll = 21
        self.makrs = 97
    
    def display(self):
        print("Name: " + self.name)
        print("Roll No: " + str(self.roll))
        print("Marks: " + str(self.makrs))

s = student("abc", 1, 1)
s.display()