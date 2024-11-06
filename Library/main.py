class Library:

    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_books(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def showInfo(self):
        print(f"The library has {self.no_of_books} books Name is :  {self.books}")


l1  = Library()
l1.add_books("Harry Porter")
l1.add_books("C++")
l1.add_books("JAVA")
l1.add_books("ORACLE")
l1.add_books("JSP")
l1.showInfo()


