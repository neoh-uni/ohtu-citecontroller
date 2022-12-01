from repositories.cite_repository import book_repository as default_book_repository
from logic import reference

# TODO: Make this universal service
class CiteService:
    def __init__(self, book_repository=default_book_repository):
        self._book_repository = book_repository

    def add_book(self, author, title, year, publisher):

        try:
            book = reference.Book(author, title, year, publisher)
            self._book_repository.new_book(book)
            # TODO: communicate with website
            print("Book added")
        except Exception as e:
            # TODO: communicate error with website
            print(e)


book_service = CiteService()

