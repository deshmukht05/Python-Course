# Accessing multiple instances
class student:
    def __init__(self, n, r, m):
        self.n = n
        self.r = r
        self.m = m
    
    def display(self):
        print("Name: ", self.n)
        print("Roll No: ", self.r)
        print("Marks: ", self.m)

s1 = student("Rohit", 1, 99)
s2 = student("Yash", 2, 98)
s3 = student("Prajwal", 3, 97)
s1.display()
s2.display()
s3.display()

# If number of students increases then above style of output cannot fit more than 5 records at a time on screen and hence need to change output format. Minor changes in above class program changes output format. 