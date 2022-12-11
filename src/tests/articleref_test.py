import unittest
from logic import reference


class TestArticle(unittest.TestCase):
    def setUp(self):
        self.valid_article = reference.Article(
            author="Pro Hackerman",
            title="What is Opsec?",
            journal="AI News",
            year=2015,
            volume="3",
            pages="44--66",
        )
        self.valid_article2 = reference.Article(
            author="Pro Hackerman",
            title="What is Opsec?",
            journal="AI News",
            year=2015,
            volume="3",
            pages="44--66",
            # optionals
            month="6",
            note="heloust this is a note",
            number="12380",
        )
        self.error_str = "a" * 5001

    def test_article_author(self):
        self.assertEqual(self.valid_article.author, "Pro Hackerman")

    def test_article_title(self):
        self.assertEqual(self.valid_article.title, "What is Opsec?")

    def test_article_journal(self):
        self.assertEqual(self.valid_article.journal, "AI News")

    def test_article_year(self):
        self.assertEqual(self.valid_article.year, 2015)
        self.assertNotEqual(self.valid_article.year, "2015")

    def test_article_volume_conversion_to_int(self):
        self.assertEqual(self.valid_article.volume, 3)
        self.assertNotEqual(self.valid_article.volume, "3")

    def test_article_pages(self):
        self.assertEqual(self.valid_article.pages, "44--66")

    # Optionals
    def test_article_note(self):
        self.assertEqual(self.valid_article2.note, "heloust this is a note")

    def test_article_month(self):
        self.assertNotEqual(self.valid_article2.month, 6)
        self.assertEqual(self.valid_article2.month, "6")

    def test_article_number(self):
        self.assertNotEqual(self.valid_article2.number, 12380)
        self.assertEqual(self.valid_article2.number, "12380")

    # ERROR raisesrs
    def test_class_errors_without_args(self):
        self.assertRaises(TypeError, reference.Article)

    def test_error_with_unexpected_len_args(self):
        self.assertRaises(
            ValueError,
            reference.Article,
            author="Pro Hackerman",
            title="What is Opsec?",
            journal=self.error_str,
            year=2015,
            volume="3",
            pages="44--66",
        )

    def test_error_with_nonalph_author(self):
        self.assertRaises(
            ValueError,
            reference.Article,
            author="Pr0 Hackerman",
            title="What is Opsec?",
            journal="AI News",
            year=2015,
            volume="3",
            pages="44--66",
        )

    def test_error_with_nonvalid_year(self):
        self.assertRaises(
            ValueError,
            reference.Article,
            author="Pro Hackerman",
            title="What is Opsec?",
            journal="AI News",
            year=100,
            volume="3",
            pages="44--66",
        )
        self.assertRaises(
            ValueError,
            reference.Article,
            author="Pro Hackerman",
            title="What is Opsec?",
            journal="AI News",
            year=9999,
            volume="3",
            pages="44--66",
        )

    def test_error_with_int_when_exptd_str(self):
        self.assertRaises(
            ValueError,
            reference.Article,
            author="Pro Hackerman",
            title="What is Opsec?",
            journal=12,
            year=2009,
            volume="3",
            pages="44--66",
        )
        self.assertRaises(
            ValueError,
            reference.Article,
            author="Pro Hackerman",
            title="What is Opsec?",
            journal="AI News",
            year=2009,
            volume="3",
            pages=2000,
        )
        self.assertRaises(
            ValueError,
            reference.Article,
            author="Pro Hackerman",
            title=1,
            journal="AI News",
            year=2009,
            volume="3",
            pages="44--66",
        )
        self.assertRaises(
            ValueError,
            reference.Article,
            author=12,
            title="mitä ikinä",
            journal="AI News",
            year=2009,
            volume="3",
            pages="44--66",
        )

    def test_error_with_int_when_exptd_str_optionals(self):
        self.assertRaises(
            ValueError,
            reference.Article,
            author="Pro Hackerman",
            title="What is Opsec?",
            journal="AI News",
            year=2009,
            volume="3",
            pages="44--66",
            month=3,
        )
        self.assertRaises(
            ValueError,
            reference.Article,
            author="Pro Hackerman",
            title="What is Opsec?",
            journal="AI News",
            year=2009,
            volume="3",
            pages="44--66",
            note=3,
        )
        self.assertRaises(
            ValueError,
            reference.Article,
            author="Pro Hackerman",
            title="What is Opsec?",
            journal="AI News",
            year=2009,
            volume="3",
            pages="44--66",
            number=3,
        )
