# Accessing parent class member in child class
class base:
    def __init__(self, a):
        self.a = a
    
class derived(base):
    def __init__(self, x, y):
        base.a = x
        self.b = y
    
    def print_sum(self):
        sum = base.a + self.b
        print("Sum: ", sum)
    
    def print_small(self):
        if base.a<self.b:
            print(base.a, " is small.")
        else:
            print(self.b, " is small")

d = derived(2, 1)
d.print_small()

# Inheritance allow us to access members of parent class by using parent class name as qualifier with (dot) membership operator.
# Alternative is using super() function.