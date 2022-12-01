from flask import render_template, redirect, request, Blueprint
from services.cite_service import cite_service


routes = Blueprint("app", __name__)

# kun ohjelma käynnistyy, niin aukee aloitus sivu. Pitäs nyt toimia.
@routes.route("/")
def index():
    return render_template("index.html")


# lukee formin tiedot
@routes.route("/createbook", methods=["POST"])
def create_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        cite_service.add_book(author, title, year, publisher)
        return redirect("/")

@routes.route("/createarticle", methods=["POST"])
def create_article():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        year = request.form["year"]
        journal = request.form["journal"]
        volume = request.form["volume"]
        pages = request.form["pages"]
        cite_service.add_article(author, title, year, journal, volume, pages)
        return redirect("/")

@routes.route("/createinproceedings", methods=["POST"])
def create_inproceedings():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        year = request.form["year"]
        booktitle = request.form["booktitle"]
        cite_service.add_inproceedings(author, title, year, booktitle)
        return redirect("/")

@routes.route("/choosesource", methods=["POST"])
def choose_source_type():

    source_type = request.form["radiobutton"]

    if source_type == "book":
        return render_template("index.html", book=True)

    if source_type == "article":
        return render_template("index.html", article=True)

    if source_type == "in_proceedings":
        return render_template("index.html", in_proceedings=True)
