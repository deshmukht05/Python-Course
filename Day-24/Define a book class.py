# Define a book class with attributes title, author and price of books. Inherit into class library that adds new attributes, number of copies of that book. Write a program to input and print book details and total stock of books in library.

class Book:
    def __init__(self, t, a, p):
        self.t = t
        self.a = a
        self.p = p
    
    def BookInfo(self):
        print("Title of Book: " + self.t)
        print("Name of author: " + self.a)
        print("Price of book: " + str(self.p))

class Library(Book):
    total=0
    def __init__(self, title, author, price, copies):
        super().__init__(title, author, price)
        self.copies = copies
        Library.total += self.copies
    
    def LibInfo(self):
        print("Total copies: " + str(self.copies))
        print()

l1 = Library("IoT", "Raj", 785, 45)
l2 = Library("React", "Suresh", 455, 20)
l3 = Library("NodeJS", "Vishal", 567, 54)

l1.BookInfo()
l1.LibInfo()
l2.BookInfo()
l2.LibInfo()
l3.BookInfo()
l3.LibInfo()

print("Total books in library: "  + str(l1.total))