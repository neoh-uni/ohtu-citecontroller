from attrs import asdict
from repositories.cite_repository import cite_repository as default_cite_repository
from logic import reference

# TODO: Make this universal service
class CiteService:
    def __init__(self, cite_repository=default_cite_repository):
        self._cite_repository = cite_repository

    def add_book(self, author, title, year, publisher):
        try:
            book = reference.Book(author, title, year, publisher)
            bibi = self.to_bibitex(book, "book")
            self._cite_repository.new_book(book, bibi)
            return "Book added"
        except ValueError as err:
            return err

    def add_article(self, author, title, year, journal, volume, pages):
        try:
            article = reference.Article(author, journal, title, year, volume, pages)
            bibi = self.to_bibitex(article, "article")
            self._cite_repository.new_article(article, bibi)
            return "Article added"
        except ValueError as err:
            return err

    def add_inproceedings(self, author, title, year, booktitle):
        try:
            inproceedings = reference.Inproceedings(author, title, year, booktitle)
            self._cite_repository.new_inproceedings(inproceedings)
            return "Inproceedings added"
        except ValueError as err:
            return err

    def get_all(self):
        return list(
            self._cite_repository.get_books(),
            self._cite_repository.get_articles(),
            self._cite_repository.get_inproceedings(),
        )

    def get_books(self):
        return self._cite_repository.get_books()

    def get_articles(self):
        return self._cite_repository.get_articles()

    def get_inproceedings(self):
        return self._cite_repository.get_inproceedings()

    def to_bibitex(self, ref, ref_type):
        non_none_attrs = [(name, value) for name,value in asdict(ref).items() if value is not None]

        bibi = f"@{ref_type}{{CITEACRONYM,\n"
        for (attribute, value) in non_none_attrs:
            bibi += "    "+attribute+" = {"+str(value)+"},\n"
        bibi += "}"
        return bibi



cite_service = CiteService()
