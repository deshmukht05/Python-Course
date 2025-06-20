# Define a polygon class to accept number of sides and input side length. Inherit polygon class to find area to triangle.
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    
    def inputSides(self):
        self.sides = [float(input("Enter side" + str(i+1) + " : ")) for i in range(self.n)]
    
    def disSides(self):
        for i in range(self.n):
            print("Side ", i+1, " is ", self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
    
    def findArea(self):
        a, b, c = self.sides

        # Calculate the semi-perimeter
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print("The area of the triangle: ", end = '')
        print("%.2f"%round(area, 2))

t = Triangle()
t.inputSides()
t.disSides()
t.findArea()