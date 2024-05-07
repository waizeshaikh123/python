class Library:
    def __init__(self):
        self.noBooks = 0
        self.book = []
    def addBooks(self,books):
        self.book.append(books)
        self.noBooks = len(self.book)
    def showBooks(self):
        print(f"The library of books is {self.noBooks} bboks are in")
        for book in self.book:
            print(book)
a = Library()
a.addBooks("waize shaikh")
a.addBooks("waize shaikh")
a.addBooks("waize shaikh")
a.showBooks()