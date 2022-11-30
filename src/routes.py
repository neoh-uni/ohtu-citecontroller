from flask import render_template, redirect, request, Blueprint

from logic.reference import Book
from services.book_service import book_service


routes = Blueprint("app", __name__)

# kun ohjelma käynnistyy, niin aukee aloitus sivu. Pitäs nyt toimia.
@routes.route("/")
def index():
    return render_template("index.html")


# lukee formin tiedot
@routes.route("/createbook", methods=["post"])
def create_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        book_service.add_book(author, title, year, publisher)
        return redirect("/")

@app.route("/choosesource", methods=["POST"])
def choose_source_type():

    source_type = request.form["radiobutton"]

    if source_type == "book":
        return render_template("test.html", book=True)

    if source_type == "article":
        return render_template("test.html", article=True)

    if source_type == "in_proceedings":
        return render_template("test.html", in_proceedings=True)