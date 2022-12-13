from app import db


class CiteRepository:
    def new_book(self, book, bibi):

        sql = """INSERT INTO cites (acronym, type, author, title, year, publisher, bibitex)
                 VALUES (:acronym, :type, :author, :title, :year, :publisher, :bibitex)"""
        db.session.execute(
            sql,
            {
                "acronym": book.acronym,
                "type": "book",
                "author": book.author,
                "title": book.title,
                "year": book.year,
                "publisher": book.publisher,
                "bibitex": bibi,
            },
        )
        db.session.commit()

    def new_article(self, article, bibi):
        sql = """INSERT INTO cites (acronym, type, author, title, year, journal, volume, pages, bibitex)
                VALUES (:acronym, :type, :author, :title, :year, :journal, :volume, :pages, :bibitex)"""
        db.session.execute(
            sql,
            {
                "acronym": article.acronym,
                "type": "article",
                "author": article.author,
                "title": article.title,
                "year": article.year,
                "journal": article.journal,
                "volume": article.volume,
                "pages": article.pages,
                "bibitex": bibi,
            },
        )
        db.session.commit()

    def new_inproceedings(self, inproceedings, bibi):
        sql = """INSERT INTO cites (acronym, type, author, title, year, booktitle, bibitex)
                VALUES (:acronym, :type, :author, :title, :year, :booktitle, :bibitex)"""
        db.session.execute(
            sql,
            {
                "acronym": inproceedings.acronym,
                "type": "inproceedings",
                "author": inproceedings.author,
                "title": inproceedings.title,
                "year": inproceedings.year,
                "booktitle": inproceedings.booktitle,
                "bibitex": bibi,
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

    def get_bibitex(self, ref_type):

        sql = "SELECT id, bibitex FROM cites WHERE type =:type"
        return db.session.execute(sql, {"type": ref_type}).fetchall()

    def get_only_bibtex(self):
        sql = "SELECT bibitex FROM cites"
        return db.session.execute(sql).fetchall()

    def get_by_id(self, id):

        sql = "SELECT * FROM cites WHERE id =:id"
        return db.session.execute(sql, {"id": id}).fetchone()


cite_repository = CiteRepository()
