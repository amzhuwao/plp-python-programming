#usr/bin/python3

"""
Create a class representing anything you like e.g smartphone, book
Add attributes and methods to bring the class to life
Use constructor to initialize each object with unique values
Add an inheritance layer to explore polymorphism or encapsulation
"""

class Book:
    def __init__(self, title, isbn, author, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        
    def details(self):
        print(f'Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nPrice: {self.price}')
        
class Text_Book(Book):
    def __init__(self, title, isbn, author, price, subject):
        super().__init__(title, isbn, author, price)
        self.subject = subject
       
Geo1 = Text_Book('Geography Matters','123','aubrey zhuwao','$30','g')

Geo1.details()