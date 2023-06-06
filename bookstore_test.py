import unittest
from bookstore import Bookstore

class TestBookstore(unittest.TestCase):

    def setUp(self):
        self.bookstore = Bookstore()
    
    def test_add_book_valid(self):
        self.bookstore.add_book("1984", "George Orwell", 8.99, 8)
        self.bookstore.add_book("The Great Gatsby", "F. Scott Fitzgerald", 19.99, 10)
        self.bookstore.add_book("To Kill a Mockingbird", "Harper Lee", 12.99, 5)
        self.assertEqual(len(self.bookstore.books), 3)

    def test_add_book_invalid(self):
        self.bookstore.add_book("The Great Gatsby", "F. Scott Fitzgerald", 19.99, 10)
        self.bookstore.add_book("To Kill a Mockingbird", "Harper Lee", 12.99, 5)
        result = self.bookstore.add_book("The Catcher in the Rye", "J.D. Salinger", -5.99, 3)
        self.assertFalse(result)
        self.assertEqual(len(self.bookstore.books), 2)


    def test_add_book_duplicate(self):
        self.bookstore.add_book("To Kill a Mockingbird", "Harper Lee", 12.99, 5)
        initial_book_count = len(self.bookstore.books)
        self.bookstore.add_book("To Kill a Mockingbird", "Harper Lee", 12.99, 5)
        self.assertEqual(len(self.bookstore.books), initial_book_count)

    def test_remove_book_valid(self):
        self.bookstore.add_book("The Great Gatsby", "F. Scott Fitzgerald", 19.99, 10)
        self.bookstore.add_book("To Kill a Mockingbird", "Harper Lee", 12.99, 5)
        self.bookstore.remove_book("The Great Gatsby")
        self.assertEqual(len(self.bookstore.books), 1)

    def test_remove_book_invalid(self):
        self.assertFalse(self.bookstore.remove_book("Pride and Prejudice"))

    def test_add_customer_valid(self):
        self.bookstore.add_customer("John")
        self.bookstore.add_customer("Jane")
        self.bookstore.add_customer("Ron")
        self.assertEqual(len(self.bookstore.customers), 3)

    def test_add_customer_invalid(self):
        self.bookstore.add_customer("John")
        self.bookstore.add_customer("Jane")
        self.bookstore.add_customer("")
        self.assertEqual(len(self.bookstore.customers), 2)

    def test_add_customer_duplicate(self):
        self.bookstore.add_customer("John")
        self.bookstore.add_customer("John")
        self.bookstore.add_customer("Jane")
        self.assertEqual(len(self.bookstore.customers), 2)

    def test_remove_customer_valid(self):
        self.bookstore.add_customer("Jane")
        self.bookstore.add_customer("John")
        self.bookstore.remove_customer("John")
        self.assertEqual(len(self.bookstore.customers), 1)

    def test_remove_customer_invalid(self):
        self.assertFalse(self.bookstore.remove_customer("Eve"))

    def test_add_to_wishlist_valid(self):
        self.bookstore.add_customer("John")
        self.bookstore.add_book("The Great Gatsby", "F. Scott Fitzgerald", 19.99, 10)
        self.bookstore.add_to_wishlist("John", "The Great Gatsby")
        self.assertEqual(len(self.bookstore.find_customer("John").wishlist), 1)

    def test_add_to_wishlist_invalid(self):
        self.bookstore.add_customer("John")
        self.bookstore.add_book("The Great Gatsby", "F. Scott Fitzgerald", 19.99, 10)
        self.bookstore.add_to_wishlist("John", "Of Mice and Men")
        self.assertEqual(len(self.bookstore.find_customer("John").wishlist), 0)

    def test_remove_from_wishlist_valid(self):
        self.bookstore.add_customer("John")
        self.bookstore.add_book("The Great Gatsby", "F. Scott Fitzgerald", 19.99, 10)
        self.bookstore.add_to_wishlist("John", "The Great Gatsby")
        self.bookstore.remove_from_wishlist("John", "The Great Gatsby")
        self.assertEqual(len(self.bookstore.find_customer("John").wishlist), 0)

    def test_remove_from_wishlist_invalid(self):
        self.bookstore.add_customer("John")
        self.bookstore.add_book("The Great Gatsby", "F. Scott Fitzgerald", 19.99, 10)
        self.bookstore.add_to_wishlist("John", "The Great Gatsby")
        self.bookstore.remove_from_wishlist("John", "Of Mice and Men")
        self.assertEqual(len(self.bookstore.find_customer("John").wishlist), 1)
