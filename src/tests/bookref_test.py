import unittest
from src.logic import reference

class TestBook(unittest.TestCase):
    def setUp(self):
        self.valid_book = reference.Book(author="Pro Coder", title="What is DevOps?", publisher="unigrafia", year=2011)
        self.error_str = "a"*5001
    def test_book_author(self):
        self.assertEqual(self.valid_book.author, "Shit Coder")
        
    def test_book_publisher(self):
        self.assertEqual(self.valid_book.publisher, "unigrafia")

    def test_book_year(self):
        self.assertEqual(self.valid_book.year, 2011)
    
    def test_book_title(self):
        self.assertEqual(self.valid_book.title, "What is DevOps?")

    def test_class_errors_without_args(self):
        self.assertRaises(TypeError, reference.Book)

    def test_error_with_unexpected_len_args(self):
        self.assertRaises(ValueError, reference.Book,author="Pro Coder", title="What is DevOps?", publisher=self.error_str, year=2011)

    def test_error_with_nonalph_name(self):
        self.assertRaises(ValueError, reference.Book,author="Pro C0der", title="What is DevOps?", publisher="unigrafia", year=2011)
