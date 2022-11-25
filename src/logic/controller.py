from reference import Book

class Controller:

    def validate(type: str, info: dict):
        # todo
        pass

    def compile_book(info: dict):
        book = Book(info["author"], info["title"], info["year"], info["publisher"])

        return book

    def add_cite(type: str):
        info = {}
        if type == "book":
            book = compile_book(info)