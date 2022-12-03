import unittest
from logic import reference


class TestBook(unittest.TestCase):
    def setUp(self):
        self.valid_book = reference.Book(
            author="Pro Coder",
            title="What is DevOps?",
            publisher="unigrafia",
            year=2011,
        )
        self.valid_book2 = reference.Book(
            author="Pro Coder",
            title="What is DevOps?",
            publisher="unigrafia",
            year=2011,
            #optionals
            address="Revontulentie 5",
            edition="99",
            editor="Esko Editti",
            month="Tammikuu",
            note="viesti sinulle",
            number="+3581234567",
            series="sarjat",
            volume="volume99",
        )
        self.error_str = "a" * 5001

    def test_book_author(self):
        self.assertEqual(self.valid_book.author, "Pro Coder")

    def test_book_publisher(self):
        self.assertEqual(self.valid_book.publisher, "unigrafia")

    def test_book_year(self):
        self.assertEqual(self.valid_book.year, 2011)

    def test_book_title(self):
        self.assertEqual(self.valid_book.title, "What is DevOps?")
    
    #Test Optionals Setup
    def test_book_address(self):
        self.assertEqual(self.valid_book2.address, "Revontulentie 5")
    
    def test_book_edition(self):
        self.assertEqual(self.valid_book2.edition, "99")
    
    def test_book_editor(self):
        self.assertEqual(self.valid_book2.editor, "Esko Editti")

    def test_book_month(self):
        self.assertEqual(self.valid_book2.month, "Tammikuu")

    def test_book_note(self):
        self.assertEqual(self.valid_book2.note, "viesti sinulle")

    def test_book_number(self):
        self.assertEqual(self.valid_book2.number, "+3581234567")

    def test_book_series(self):
        self.assertEqual(self.valid_book2.series, "sarjat")

    def test_book_volume(self):
        self.assertEqual(self.valid_book2.volume, "volume99")

    def test_class_errors_without_args(self):
        self.assertRaises(TypeError, reference.Book)

    #Test Error raisers
    def test_error_with_unexpected_len_args(self):
        self.assertRaises(
            ValueError,
            reference.Book,
            author="Pro Coder",
            title="What is DevOps?",
            publisher=self.error_str,
            year=2011,
        )

    def test_error_with_nonalph_name(self):
        self.assertRaises(
            ValueError,
            reference.Book,
            author="Pro C0der",
            title="What is DevOps?",
            publisher="unigrafia",
            year=2011,
        )

    def test_error_with_nonvalid_year(self):
        self.assertRaises(
            ValueError,
            reference.Book,
            author="Pro Coder",
            title="What is DevOps?",
            publisher="unigrafia",
            year=300,
        )
        self.assertRaises(
            ValueError,
            reference.Book,
            author="Pro Coder",
            title="What is DevOps?",
            publisher="unigrafia",
            year=5000,
        )

    def test_error_with_int_when_exptd_str(self):
        self.assertRaises(
            TypeError,
            reference.Book,
            author=1,
            title="What is DevOps?",
            publisher="unigrafia",
            year=2000,
        )
        self.assertRaises(
            TypeError,
            reference.Book,
            author="Pro Coder",
            title=2,
            publisher="unigrafia",
            year=2000,
        )
        self.assertRaises(
            TypeError,
            reference.Book,
            author="Pro Coder",
            title="What is DevOps?",
            publisher=3,
            year=2000,
        )

    def test_error_with_int_when_exptd_str_optionals(self):
        self.assertRaises(
            ValueError,
            reference.Book,
            author="Pro Coder",
            title="What is DevOps?",
            publisher="unigrafia",
            year=2000,
            month=99
        )
        self.assertRaises(
            ValueError,
            reference.Book,
            author="Pro Coder",
            title="What is DevOps?",
            publisher="unigrafia",
            year=2000,
            note=2000
        )