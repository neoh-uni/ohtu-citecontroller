from flask import render_template, redirect, request, Blueprint, flash
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
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        year = request.form["year"].strip()
        publisher = request.form["publisher"].strip()
        msg = cite_service.add_book(author, title, year, publisher)
        return render_template("index.html", message=msg)


@routes.route("/createarticle", methods=["POST"])
def create_article():
    if request.method == "POST":
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        year = request.form["year"].strip()
        journal = request.form["journal"].strip()
        volume = request.form["volume"].strip()
        pages = request.form["pages"].strip()
        msg = cite_service.add_article(author, title, year, journal, volume, pages)
        return render_template("index.html", message=msg)


@routes.route("/createinproceedings", methods=["POST"])
def create_inproceedings():
    if request.method == "POST":
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        year = request.form["year"].strip()
        booktitle = request.form["booktitle"].strip()
        msg = cite_service.add_inproceedings(author, title, year, booktitle)
        return render_template("index.html", message=msg)


@routes.route("/choosesource", methods=["POST"])
def choose_source_type():

    source_type = request.form["radiobutton"]

    if source_type == "book":
        return render_template("index.html", book=True)

    if source_type == "article":
        return render_template("index.html", article=True)

    if source_type == "in_proceedings":
        return render_template("index.html", in_proceedings=True)


@routes.route("/references", methods=["GET"])
def references():
    return render_template("references.html")


@routes.route("/display_references", methods=["POST"])
def display_references():

    books = cite_service.get_books()
    articles = cite_service.get_articles()
    in_proceedings = cite_service.get_inproceedings()

    display_type = request.form["radiobutton"]

    if display_type == "all":
        return render_template(
            "references.html",
            books=books,
            articles=articles,
            in_proceedings=in_proceedings,
            all=True,
        )

    if display_type == "bibitext":
        return render_template(
            "references.html",
            books=books,
            articles=articles,
            in_proceedings=in_proceedings,
            bibitex=True,
        )

@routes.route("/search", methods=["POST"])
def search():

    keyword = request.form["keyword"]

    books = cite_service.book_search2(keyword)
    articles = cite_service.article_search2(keyword)
    in_proceedings = cite_service.in_proceedings_search2(keyword)

    if books is None and articles is None and in_proceedings is None:
        flash("No searches found")
        return render_template("references.html")
    else:
        return render_template(
            "references.html",
            books=books, 
            articles=articles,
            in_proceedings=in_proceedings,
            all=True
        )

