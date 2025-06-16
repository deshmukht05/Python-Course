# Creating and printing instance
class vehicle:
    max_speed = 180
    def describe(self, m, y, p):
        print("This is " + m + " of year " + str(y))
        print("It costs INR" + str(p))
        print("Maximum speed is " + str(self.max_speed))

car = vehicle()
car.describe("Vista", 2010, 550000)

# car is instance of vehicle
# max_speed is instance attribute
# describe() is class method
# m, y, p are local variables of method
# Local variables are accessed directly whereas instance attribute is accessed using self. 