class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
    
class Customer:
    def __init__(self, name):
        self.name = name
        self.wishlist = []

    def addToWishlist(self, book):
        self.wishlist.append(book)

    def removeFromWishlist(self, title):
        for book in self.wishlist:
            if book.title.lower() == title.lower():
                self.wishlist.remove(book)
                return True
        return False

class Bookstore:
    def __init__(self):
        self.books = []
        self.customers = []

    def add_book(self, title, author, price, stock):
        if price >= 0 and stock > 0 and self.find_book(title) is None and title and author:
            book = Book(title, author, price, stock)
            self.books.append(book)
            return True
        else:
            return False


    def remove_book(self, title):
        book = self.find_book(title)
        if book is not None:
            self.books.remove(book)
            return True
        else:
            return False

    def add_customer(self, name):
        if self.find_customer(name) is None and name:
            customer = Customer(name)
            self.customers.append(customer)
            return True
        else:
            return False

    def remove_customer(self, name):
        customer = self.find_customer(name)
        if customer is not None:
            self.customers.remove(customer)
            return True
        else:
            return False

    def add_to_wishlist(self, customer_name, title):
        customer = self.find_customer(customer_name)
        book = self.find_book(title)
        if customer is not None and book is not None:
            customer.addToWishlist(book)
            return True
        else:
            return False

    def remove_from_wishlist(self, customer_name, title):
        customer = self.find_customer(customer_name)
        if customer is not None:
            return customer.removeFromWishlist(title)
        else:
            return False

    def find_customer(self, name):
        for customer in self.customers:
            if customer.name.lower() == name.lower():
                return customer
        return None

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
