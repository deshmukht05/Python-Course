# Define a circle class with attribute radius with function to calculate area. Inherit circle class to calculate volume of cylinder.
class circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r
        self.a = 0
    
    def area(self): 
        a = self.pi*self.r*self.r
        return a
    
class cylinder(circle):
    def __init__(self, r, h):
        super().__init__(r)
        a = super().area()
        print("Area of base of cylinder: %.2f"%round(a, 2))
        self.v = a*h
    
    def volume(self):
        print("Volume of cylinder: ", end = '')
        print("%.2f"%round(self.v, 2))

c1 = cylinder(2, 10)
c1.area()
c1.volume()