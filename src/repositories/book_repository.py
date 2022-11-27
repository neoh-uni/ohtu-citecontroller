from app import db
#from logic.reference import Book

class BookRepository:
    def new_book(self, author, title, year, publisher):
        # tähän Book
        sql = """INSERT INTO books (author, title, year, publisher)
                 VALUES (:author, :title, :year, :publisher)"""
        db.session.execute(sql, {"author":author, "title":title, "year":year, "publisher":publisher})
        db.session.commit()
    
    def get_books():
        sql = "SELECT author, title, year, publisher FROM books"
        return db.session.execute(sql).fetchall()

book_repository = BookRepository()
