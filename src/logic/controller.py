from reference import Book
from services.book_service import book_service as default_book_service

class UserInputError(Exception):
    pass

class Controller:

    def __init__(self, book_service=default_book_service):
        self.book_service = book_service

    def validate_book(info: dict):
        if "author" not in info:
            raise UserInputError("Book must have an author")

        if info["author"] == None:
            raise UserInputError("Book must have an author")

        if "title" not in info:
            raise UserInputError("Book must have a title")

        if info["title"] == None:
            raise UserInputError("Book must have a title")

        if "year" not in info:
            raise UserInputError("Book must have a year")

        if info["year"] == None:
            raise UserInputError("Book must have a year")

        if "publisher" not in info:
            raise UserInputError("Book must have a publisher")

        if info["publisher"] == None:
            raise UserInputError("Book must have a publisher")


    def compile_book(info: dict):
        book = Book(info["author"], info["title"], info["year"], info["publisher"])

        return book

    def add_cite(self, type: str, info: dict):
        if type == "book":
            validate_book(info)
            book = compile_book(info)
            self.book_service.add_book(book)
