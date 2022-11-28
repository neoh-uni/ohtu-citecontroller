from app import db


class BookRepository:
    def new_book(self, author, title, year, publisher):
        sql = """INSERT INTO books (author, title, year, publisher)
                 VALUES (:author, :title, :year, :publisher)"""
        db.session.execute(
            sql,
            {"author": author, "title": title, "year": year, "publisher": publisher},
        )
        db.session.commit()


book_repository = BookRepository()
