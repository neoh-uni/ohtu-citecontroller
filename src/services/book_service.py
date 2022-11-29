from repositories.book_repository import book_repository as default_book_repository
from logic import reference

class BookService:
    def __init__(self, book_repository=default_book_repository):
        self._book_repository = book_repository
        

    def add_book(self, author, title, year, publisher):
        # tähän Book
        e = "book added"

        try:
            book = reference.Book(author, title, year, publisher)
            self._book_repository.new_book(book)
        except Exception as e:
            print(e)
        
        return e



book_service = BookService()

