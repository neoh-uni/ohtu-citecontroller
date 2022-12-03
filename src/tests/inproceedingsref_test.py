import unittest
from logic import reference


class TestInproceedings(unittest.TestCase):
    def setUp(self):
        self.valid_inproceedings = reference.Inproceedings(
            author="Nonplayer character",
            title="Game of the Year",
            year=2020,
            booktitle="diipa2' daapa",
        )
        self.valid_inproceedings2 = reference.Inproceedings(
            author="Nonplayer characted",
            title="Game of the Year",
            year=2020,
            booktitle="diipa2' daapa",
            # optionals
            address="Osoite 6500",
            editor="Jarkko Jarkkonen",
            month="Kesäkuu",
            note="muistilappu",
            number="+358500500500",
            organization="Jokin Org",
            pages="15000",
            publisher="HYY",
            series="sarjat",
            volume="volyymi==800",
        )
        self.error_str = "a" * 5001

    def test_inproceedings_author(self):
        self.assertEqual(self.valid_inproceedings.author, "Nonplayer character")

    def test_inproceedings_title(self):
        self.assertEqual(self.valid_inproceedings.title, "Game of the Year")

    def test_inproceedings_year(self):
        self.assertEqual(self.valid_inproceedings.year, 2020)
        self.assertNotEqual(self.valid_inproceedings.year, "2020")

    def test_inproceedings_booktitle(self):
        self.assertLessEqual(self.valid_inproceedings.booktitle, "diipa2' daapa")

    # Test optional args setup
    def test_inproceedings_adress(self):
        self.assertEqual(self.valid_inproceedings2.address, "Osoite 6500")

    def test_inproceedings_editor(self):
        self.assertEqual(self.valid_inproceedings2.editor, "Jarkko Jarkkonen")

    def test_inproceedings_month(self):
        self.assertEqual(self.valid_inproceedings2.month, "Kesäkuu")

    def test_inproceedings_note(self):
        self.assertEqual(self.valid_inproceedings2.note, "muistilappu")

    def test_inproceedings_number(self):
        self.assertEqual(self.valid_inproceedings2.number, "+358500500500")

    def test_inproceedings_organization(self):
        self.assertEqual(self.valid_inproceedings2.organization, "Jokin Org")

    def test_inproceedings_pages(self):
        self.assertEqual(self.valid_inproceedings2.pages, "15000")

    def test_inproceedings_publisher(self):
        self.assertEqual(self.valid_inproceedings2.publisher, "HYY")

    def test_inproceedings_series(self):
        self.assertEqual(self.valid_inproceedings2.series, "sarjat")

    def test_inproceedings_volume(self):
        self.assertEqual(self.valid_inproceedings2.volume, "volyymi==800")

    # Test Error raisers
    def test_class_errors_without_args(self):
        self.assertRaises(TypeError, reference.Inproceedings)

    def test_error_with_unexpected_len_args(self):
        self.assertRaises(
            ValueError,
            reference.Inproceedings,
            author="Nonplayer character",
            title=self.error_str,
            year=2020,
            booktitle="diipa2' daapa",
        )

    def test_error_with_nonalph_author(self):
        self.assertRaises(
            ValueError,
            reference.Inproceedings,
            author="N0nplayer character",
            title="Game of the Year",
            year=2020,
            booktitle="diipa2' daapa",
        )

    def test_error_with_nonvalid_year(self):
        self.assertRaises(
            ValueError,
            reference.Inproceedings,
            author="Nonplayer character",
            title="Game of the Year",
            year=9999,
            booktitle="diipa2' daapa",
        )
        self.assertRaises(
            ValueError,
            reference.Inproceedings,
            author="Nonplayer character",
            title="Game of the Year",
            year=15,
            booktitle="diipa2' daapa",
        )

    def test_error_with_int_when_exptd_str(self):
        self.assertRaises(
            TypeError,
            reference.Inproceedings,
            author="Nonplayer character",
            title=1,
            year=2020,
            booktitle="diipa2' daapa",
        )
        self.assertRaises(
            TypeError,
            reference.Inproceedings,
            author=1,
            title="Game of the Year",
            year=2020,
            booktitle="diipa2' daapa",
        )
        self.assertRaises(
            TypeError,
            reference.Inproceedings,
            author="Nonplayer character",
            title="Game of the Year",
            year=2020,
            booktitle=1,
        )

    def test_error_with_int_when_exptd_str_optionals(self):
        self.assertRaises(
            ValueError,
            reference.Inproceedings,
            author="Nonplayer character",
            title="Game of the Year",
            year=2020,
            booktitle="1",
            volume=1,
        )
        self.assertRaises(
            ValueError,
            reference.Inproceedings,
            author="Nonplayer character",
            title="Game of the Year",
            year=2020,
            booktitle="1",
            volume="1",
            note=99,
        )
