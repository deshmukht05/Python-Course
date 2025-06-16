# Display instance member in tabular form. 
class student:
    def __init__(self, n, r, m):
        self.n = n
        self.r = r
        self.m = m
    
    def display(self):
        print(str(self.r) + "\t" + self.n + "\t\t" + str(self.m))

s1 = student("Rohit", 1, 99)
s2 = student("Yash", 2, 98)
s3 = student("Prajwal", 3, 97)
print("RNo\tName\t\tMarks")
s1.display()
s2.display()
s3.display()