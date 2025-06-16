# Assigning value to instance local variable
class student:
    def __init__(self, n, r, m):
        self.n = n
        self.r = r
        self.m = m
    
    def display(self):
        print("Name: ", self.n)
        print("Roll No: ", self.r)
        print("Marks: ", self.m)

s = student("Rohit", 21, 98)
s.display()

# In the above program, note that when object is created only two values are passed whereas values of third variable is assigned in the method __init__()