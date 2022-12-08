from flask import render_template, request, Blueprint
from services.cite_service import cite_service

MISSING_FIELD = "All fields must have a value"

routes = Blueprint("app", __name__)

# kun ohjelma käynnistyy, niin aukee aloitus sivu. Pitäs nyt toimia.
@routes.route("/")
def index():
    return render_template("index.html")


# lukee formin tiedot
@routes.route("/createbook", methods=["POST"])
def create_book():
    if request.method == "POST":
        book_required_fields = ["author", "publisher", "title", "year"]
        clf, req_fields = check_field_remove_whitespace(
            request.form, book_required_fields
        )
        if req_fields:
            msg = cite_service.add_book(
                author=clf["author"],
                publisher=clf["publisher"],
                title=clf["title"],
                year=clf["year"],
            )
        else:
            msg = MISSING_FIELD
        return render_template("index.html", message=msg)


@routes.route("/createarticle", methods=["POST"])
def create_article():
    if request.method == "POST":
        article_required_fields = [
            "author",
            "journal",
            "pages",
            "title",
            "volume",
            "year",
        ]

        clf, req_fields = check_field_remove_whitespace(
            request.form, article_required_fields
        )

        if req_fields:
            msg = cite_service.add_article(
                author=clf["author"],
                journal=clf["journal"],
                pages=clf["pages"],
                title=clf["title"],
                year=clf["volume"],
                volume=["year"],
            )
        else:
            msg = MISSING_FIELD
        return render_template("index.html", message=msg)


@routes.route("/createinproceedings", methods=["POST"])
def create_inproceedings():
    if request.method == "POST":
        inproc_required_fields = ["author", "booktitle", "title", "year"]

        clf, req_fields = check_field_remove_whitespace(
            request.form, inproc_required_fields
        )
        if req_fields:
            msg = cite_service.add_inproceedings(
                author=clf["author"],
                booktitle=clf["booktitle"],
                title=clf["title"],
                year=clf["year"],
            )
        else:
            msg = MISSING_FIELD
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


def check_field_remove_whitespace(form: dict, check_list: list):
    for att in check_list:
        if form[att] == "":
            return form, False
        form[att].strip()
    return form, True
