import unittest
from logic.controller import Controller
from logic.reference import Book


class TestController(unittest.TestCase):
    def setUp(self):
        self.valid_book = {
            "author": "Pro Coder",
            "title": "What is DevOps?",
            "year": 2011,
            "publisher": "unigrafia",
        }
        self.controller = Controller()

    def test_constructor_assigns_book_service(self):
        self.assertIsNotNone(self.controller.book_service)

    def test_compile_book_creates_right_valid_book(self):
        book = self.controller.compile_book(self.valid_book)

        self.assertIsInstance(book, Book)
        self.assertEqual(book.author, "Pro Coder")
        self.assertEqual(book.year, 2011)
