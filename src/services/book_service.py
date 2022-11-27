from repositories.book_repository import book_repository as default_book_repository


class BookService:
    def __init__(self, book_repository=default_book_repository):
        self._book_repository = book_repository
    
    def add_book(self, author, title, year, publisher):
        # tähän Book
        return self._book_repository.new_book(author, title, year, publisher)
  

book_service = BookService()
