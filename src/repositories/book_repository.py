from app import db


class BookRepository:
    def new_book(self, book):
        
        sql = """INSERT INTO books (author, title, year, publisher)
                 VALUES (:author, :title, :year, :publisher)"""
        db.session.execute(
            sql,
            {"author": book.author, "title": book.title, "year": book.year, "publisher": book.publisher},
        )
        db.session.commit()


book_repository = BookRepository()
