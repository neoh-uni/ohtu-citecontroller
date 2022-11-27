from flask import render_template, redirect, request, Blueprint
#from logic.reference import Book
from services.book_service import book_service


routes = Blueprint("app", __name__)

# kun ohjelma käynnistyy, niin aukee aloitus sivu. Pitäs nyt toimia.
@routes.route("/")
def index():
    return render_template("index.html")

# lukee formin tiedot
@routes.route("/createsource", methods=["post"])
def create_book():
    if request.method == "POST":
        title = request.form["book_name"]
        author = request.form["author"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        book_service.add_book(author, title, year, publisher)
        return redirect ("/")

    """ En saanut importattua book
       book = Book(author, title, year, publisher)
       book_service.add_book(book)"""
