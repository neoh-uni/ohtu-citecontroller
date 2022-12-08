from app import db


class CiteRepository:
    def new_book(self, book, bibi):

        sql = """INSERT INTO cites (type, author, title, year, publisher, bibitex)
                 VALUES (:type, :author, :title, :year, :publisher, :bibitex)"""
        db.session.execute(
            sql,
            {
                "type": "book",
                "author": book.author,
                "title": book.title,
                "year": book.year,
                "publisher": book.publisher,
                "bibitex": bibi
            },
        )
        db.session.commit()

    def new_article(self, article, bibi):
        sql = """INSERT INTO cites (type, author, title, year, journal, volume, pages, bibitex)
                VALUES (:type, :author, :title, :year, :journal, :volume, :pages, :bibitex)"""
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
                "bibitex": bibi
            },
        )
        db.session.commit()

    def new_inproceedings(self, inproceedings, bibi):
        sql = """INSERT INTO cites (type, author, title, year, booktitle, bibitex)
                VALUES (:type, :author, :title, :year, :booktitle, :bibitex)"""
        db.session.execute(
            sql,
            {
                "type": "inproceedings",
                "author": inproceedings.author,
                "title": inproceedings.title,
                "year": inproceedings.year,
                "booktitle": inproceedings.booktitle,
                "bibitex": bibi
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


    def book_search(self, keyword):

        result = []
        is_int = False
        try:
            int(keyword)
            is_int = True
        except:
            pass

        if is_int:
            result.append(self.search_field("id", int(keyword), "book"))
            result.append(self.search_field("year", int(keyword), "book"))

        result.append(self.search_field("title", keyword, "book"))
        result.append(self.search_field("author", keyword, "book"))
        result.append(self.search_field("publisher", keyword, "book"))

        result_ids = []
        final_result = []
        for find in result:
            if find[0] not in result_ids:
                final_result.append(find)
                result_ids.append(find[0])
        
        return final_result

    def article_search(self, keyword):
        
        result = []
        is_int = False
        try:
            int(keyword)
            is_int = True
        except:
            pass

        if is_int:
            result.append(self.search_field("id", int(keyword), "article"))
            result.append(self.search_field("year", int(keyword), "article"))
        
        result.append(self.search_field("title", keyword, "article"))
        result.append(self.search_field("author", keyword, "article"))
        result.append(self.search_field("volume", keyword, "article"))
        result.append(self.search_field("journal", keyword, "article"))
        result.append(self.search_field("pages", keyword, "article"))


        result_ids = []
        final_result = []
        for find in result:
            if find[0] not in result_ids:
                final_result.append(find)
                result_ids.append(find[0])
        
        return final_result

    def in_proceedings_search(self, keyword):

        result = []
        is_int = False
        try:
            int(keyword)
            is_int = True
        except:
            pass

        if is_int:
            result.append(self.search_field("id", int(keyword), "inproceedings"))
            result.append(self.search_field("year", int(keyword), "inproceedings"))

        result.append(self.search_field("title", keyword, "inproceedings"))
        result.append(self.search_field("author", keyword, "inproceedings"))
        result.append(self.search_field("booktitle", keyword, "inproceedings"))

        result_ids = []
        final_result = []
        for find in result:
            if find[0] not in result_ids:
                final_result.append(find)
                result_ids.append(find[0])
        
        return final_result

    def search_field(self, field, keyword, type):
        
        sql = f"SELECT * FROM cites WHERE {field} LIKE '{keyword}' AND type = {type}"
        result = db.session.execute(sql)
        
        return result



    def delete_all(self):
        sql = """DELETE FROM cites"""
        db.session.execute(sql)
        db.session.commit()

    
    def get_bibitex(self, type):
        
        sql = "SELECT id, bibitex FROM cites WHERE type =:type"
        return db.session.execute(sql, {"type":type}).fetchall()


    def get_by_id(self, id):

        sql = "SELECT * FROM cites WHERE id =:id"
        return db.session.execute(sql, {"id":id}).fetchone()

cite_repository = CiteRepository()
