from app import db


class CiteRepository:
    def new_book(self, book):
        
        sql = """INSERT INTO cites (type, author, title, year, publisher)
                 VALUES (:type, :author, :title, :year, :publisher)"""
        db.session.execute(
            sql,
            {"type": "book", "author": book.author, "title": book.title, "year": book.year, "publisher": book.publisher},
        )
        db.session.commit()

    def new_article(self, article):
        sql = """INSERT INTO cites (type, author, title, year, journal, volume, pages)
                VALUES (:type, :author, :title, :year, :journal, :volume, :pages)"""
        db.session.execute(
            sql,
            {"type": "article", "author": article.author, "title": article.title, "year": article.year, "journal": article.journal, 
            "volume": article.volume, "pages": article.pages},
        )
        db.session.commit()
    
    def new_inproceedings(self, inproceedings):
        sql = """INSERT INTO cites (type, author, title, year, journal, volume, pages)
                VALUES (:type, :author, :title, :year, :journal, :volume, :pages)"""
        db.session.execute(
            sql,
            {"type": "inproceedings", "author": inproceedings.author, "title": inproceedings.title, "year": inproceedings.year, "booktitle": inproceedings.booktitle},
        )
        db.session.commit()


cite_repository = CiteRepository()
