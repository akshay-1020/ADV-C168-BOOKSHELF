import datetime
class Bookshelf:
    def __init__(self,name,author,price,pubyear):
        self.name = name
        self.author = author
        self.price = price
        self.pubyear = pubyear
    def add_book(self):
        print("The name of the book is " + str(self.name))
        print("The author is " + str(self.author) + ".")
        print("The price of the book is " + str(self.price) + ".")
        print("The book was published in " + str(self.pubyear) + ".")
        print("Book Added \n  ")
    def yrsincepub(self):
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        yearc = date.strftime("%Y")
        yearsago = int(yearc) - self.pubyear
        print("This book was published " + str(yearsago) + " years ago.")
obj1 = Bookshelf("Harry Potter and the Philosopher's stone.", "J.K. Rowling", 1928, 1997)
obj1.add_book()
obj1.yrsincepub()

obj2 = Bookshelf("Harry Potter and the Philosopher's stone.", "J.K. Rowling", 1928, 1997)
obj2.add_book()
obj2.yrsincepub()