from repositories.book_repository import book_repository as default_book_repository
from logic.controller import Controller

class BookService:
    def __init__(self, book_repository=default_book_repository):
        self._book_repository = book_repository
        self.c = Controller()


    def add_book(self, author, title, year, publisher):
        # tähän Book
        return self._book_repository.new_book(self.c.add_cite("book", {"author": author, "title": title, "year": year, "publisher": publisher}))


book_service = BookService()
