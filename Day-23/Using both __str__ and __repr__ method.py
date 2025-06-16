# Using both __str__ and __repr__ method
class student:
    def __init__(self, n, r, m):
        self.n = n
        self.r = r
        self.m = m
    
    def __repr__(self):
        return ("A")

    def __str__(self):
        return ("B")

s = student("Abhay", 1, 90)
print(s)
print(str(s))
print(repr(s))