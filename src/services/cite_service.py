from repositories.cite_repository import cite_repository as default_cite_repository
from logic import reference

# TODO: Make this universal service
class CiteService:
    def __init__(self, cite_repository=default_cite_repository):
        self._cite_repository = cite_repository

    def add_book(self, author, title, year, publisher):

        try:
            book = reference.Book(author, title, year, publisher)
            self._cite_repository.new_book(book)
            # TODO: communicate with website
            print("Book added")
        except Exception as e:
            # TODO: communicate error with website
            print(e)


cite_service = CiteService()

