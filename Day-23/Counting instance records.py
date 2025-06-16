# Counting instance records
class BookShop:
    total = 0
    def __init__(self, t, a, p):
        self.t = t
        self.a = a
        self.p = p
        BookShop.total += 1
    
    def bookInfo(self):
        print("Title of book: " + self.t)
        print("Name of author: " + self.a)
        print("Price of book: " + str(self.p))
        print()

b1 = BookShop("IoT", "Raj", 800)
b2 = BookShop("Science", "Summit", 560)
b3 = BookShop("Maths", "Vishal", 480)
b1.bookInfo()
b2.bookInfo()
b3.bookInfo()