import unittest
from logic import reference


class TestBook(unittest.TestCase):
    def setUp(self):
        self.valid_book = reference.Book(
            acronym="Coder11",
            author="Pro Coder",
            title="What is DevOps?",
            year=2011,
            publisher="unigrafia",
        )
        self.valid_book2 = reference.Book(
            acronym="Coder11",
            author="Pro Coder",
            title="What is DevOps?",
            year=2011,
            publisher="unigrafia",
            # optionals
            address="Revontulentie 5",
            edition="99",
            editor="Esko Editti",
            month="Tammikuu",
            note="viesti sinulle",
            number="+3581234567",
            series="sarjat",
            volume="99",
        )
        self.error_str = "a" * 5001

    def test_book_acronym(self):
        self.assertEqual(self.validate_book.acronym, "Coder11")

    def test_book_author(self):
        self.assertEqual(self.valid_book.author, "Pro Coder")

    def test_book_publisher(self):
        self.assertEqual(self.valid_book.publisher, "unigrafia")

    def test_book_year(self):
        self.assertEqual(self.valid_book.year, 2011)

    def test_book_title(self):
        self.assertEqual(self.valid_book.title, "What is DevOps?")

    # Test Optionals Setup
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

    def test_book_volume_to_int(self):
        self.assertEqual(self.valid_book2.volume, 99)

    def test_class_errors_without_args(self):
        self.assertRaises(TypeError, reference.Book)

    # Test Error raisers
    def test_error_with_unexpected_len_args(self):
        self.assertRaises(
            ValueError,
            reference.Book,
            acronym="Coder11",
            author="Pro Coder",
            title="What is DevOps?",
            year=2011,
            publisher=self.error_str,
        )

    def test_error_with_nonalph_name(self):
        self.assertRaises(
            ValueError,
            reference.Book,
            acronym="Coder11",
            author="Pro C0der",
            title="What is DevOps?",
            year=2011,
            publisher="unigrafia",
        )

    def test_error_with_nonvalid_year(self):
        self.assertRaises(
            ValueError,
            reference.Book,
            acronym="Coder11",
            author="Pro Coder",
            title="What is DevOps?",
            year=300,
            publisher="unigrafia",
        )
        self.assertRaises(
            ValueError,
            reference.Book,
            acronym="Coder11",
            author="Pro Coder",
            title="What is DevOps?",
            year=5000,
            publisher="unigrafia",
        )

    def test_error_with_int_when_exptd_str(self):

        self.assertRaises(
            ValueError,
            reference.Book,
            acronym=2011,
            author="Pro Coder",
            title="What is DevOps?",
            year=2000,
            publisher="unigrafia",
        )

        self.assertRaises(
            ValueError,
            reference.Book,
            acronym="Coder11",
            author=1,
            title="What is DevOps?",
            year=2000,
            publisher="unigrafia",
        )
        self.assertRaises(
            ValueError,
            reference.Book,
            acronym="Coder11",
            author="Pro Coder",
            title=2,
            year=2000,
            publisher="unigrafia",
        )
        self.assertRaises(
            ValueError,
            reference.Book,
            acronym="Coder11",
            author="Pro Coder",
            title="What is DevOps?",
            year=2000,
            publisher=3,
        )

    def test_error_with_int_when_exptd_str_optionals(self):
        self.assertRaises(
            ValueError,
            reference.Book,
            acronym="Coder11",
            author="Pro Coder",
            title="What is DevOps?",
            year=2000,
            publisher="unigrafia",
            month=99,
        )
        self.assertRaises(
            ValueError,
            reference.Book,
            acronym="Coder11",
            author="Pro Coder",
            title="What is DevOps?",
            year=2000,
            publisher="unigrafia",
            note=2000,
        )
