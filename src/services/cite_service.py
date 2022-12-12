from attrs import asdict
from repositories.cite_repository import cite_repository as default_cite_repository
from logic import reference
from pathlib import Path


class CiteService:
    def __init__(self, cite_repository=default_cite_repository):
        self._cite_repository = cite_repository

    def add_book(self, acronym, author, title, year, publisher):
        try:
            book = reference.Book(acronym, author, title, year, publisher)
            bibi = self.to_bibitex(book, "book")
            self._cite_repository.new_book(book, bibi)
            return "Book added"
        except ValueError as err:
            return err

    def add_article(self, acronym, author, title, year, journal, volume, pages):
        try:
            article = reference.Article(acronym, author, journal, title, year, volume, pages)
            bibi = self.to_bibitex(article, "article")
            self._cite_repository.new_article(article, bibi)
            return "Article added"
        except ValueError as err:
            return err

    def add_inproceedings(self, acronym, author, title, year, booktitle):
        try:
            inproceedings = reference.Inproceedings(acronym, author, title, year, booktitle)
            bibi = self.to_bibitex(inproceedings, "inproceedings")
            self._cite_repository.new_inproceedings(inproceedings, bibi)
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
        non_none_attrs = [
            (name, value) for name, value in asdict(ref).items() if value is not None
        ]

        bibi = f"@{ref_type}{{{ref.acronym},\n"
        for (attribute, value) in non_none_attrs:
            if attribute != "acronym":
                bibi += "    " + attribute + " = {" + str(value) + "},\n"
        bibi += "}"
        return bibi
        
    def all_bibtex_out(self):
        bibtexs = self._cite_repository.get_only_bibtex()
        with open("references.bib", "w", encoding="utf-8") as f:
            for bib in bibtexs:
               f.write(bib.bibitex)
               f.write("\n\n")
        return Path().absolute() / "references.bib"


    def book_search(self, keyword):

        return self._cite_repository.book_search(keyword)

    def article_search(self, keyword):

        return self._cite_repository.article_search(keyword)

    def in_proceedings_search(self, keyword):

        return self._cite_repository.in_proceedings_search(keyword)

    def book_search2(self, keyword):

        books = self._cite_repository.get_bibitex("book")
        result = []
        for book in books:
            if self.match(keyword, book[1]):
                result.append(self._cite_repository.get_by_id(book[0]))

        return result

    def article_search2(self, keyword):

        articles = self._cite_repository.get_bibitex("article")
        result = []
        for article in articles:
            if self.match(keyword, article[1]):
                result.append(self._cite_repository.get_by_id(article[0]))

        return result

    def in_proceedings_search2(self, keyword):

        in_proceedings = self._cite_repository.get_bibitex("inproceedings")
        result = []

        for in_proceeding in in_proceedings:
            if self.match(keyword, in_proceeding[1]):
                result.append(self._cite_repository.get_by_id(in_proceeding[0]))

        return result

    def match(self, keyword, bibitex):

        if keyword.lower() in bibitex.lower():
            print(keyword, bibitex)
            return True

        return False


cite_service = CiteService()
