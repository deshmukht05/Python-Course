# Working of super() function
class base:
    a = 0
    def __init__(self, a):
        self.a = a

class derived(base):
    def __init__(self, x, y):
        super().__init__(x)
        self.b = y
    
    def print_sum(self):
        self.s = self.a + self.b
        print("Sum = ", self.s)

d = derived(1, 2)
d.print_sum()