from app import db


class CiteRepository:
    def new_book(self, book):

        sql = """INSERT INTO cites (type, author, title, year, publisher)
                 VALUES (:type, :author, :title, :year, :publisher)"""
        db.session.execute(
            sql,
            {
                "type": "book",
                "author": book.author,
                "title": book.title,
                "year": book.year,
                "publisher": book.publisher,
            },
        )
        db.session.commit()

    def new_article(self, article):
        sql = """INSERT INTO cites (type, author, title, year, journal, volume, pages)
                VALUES (:type, :author, :title, :year, :journal, :volume, :pages)"""
        db.session.execute(
            sql,
            {
                "type": "article",
                "author": article.author,
                "title": article.title,
                "year": article.year,
                "journal": article.journal,
                "volume": article.volume,
                "pages": article.pages,
            },
        )
        db.session.commit()

    def new_inproceedings(self, inproceedings):
        sql = """INSERT INTO cites (type, author, title, year, booktitle)
                VALUES (:type, :author, :title, :year, :booktitle)"""
        db.session.execute(
            sql,
            {
                "type": "inproceedings",
                "author": inproceedings.author,
                "title": inproceedings.title,
                "year": inproceedings.year,
                "booktitle": inproceedings.booktitle,
            },
        )
        db.session.commit()

    def get_books(self):
        sql = """SELECT * FROM cites WHERE type='book'"""
        return db.session.execute(sql).fetchall()

    def get_articles(self):
        sql = """SELECT * FROM cites WHERE type='article'"""
        return db.session.execute(sql).fetchall()

    def get_inproceedings(self):
        sql = """SELECT * FROM cites WHERE type='inproceedings'"""
        return db.session.execute(sql).fetchall()

    def delete_all(self):
        sql = """DELETE FROM cites"""
        db.session.execute(sql)
        db.session.commit()


cite_repository = CiteRepository()
