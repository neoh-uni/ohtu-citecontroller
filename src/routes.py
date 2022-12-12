from flask import render_template, request, Blueprint, flash, send_file
from services.cite_service import cite_service 
from services.doi_service import doi_service

MISSING_FIELD = "All fields must have a value"

routes = Blueprint("app", __name__)

# kun ohjelma käynnistyy, niin aukee aloitus sivu. Pitäs nyt toimia.
@routes.route("/")
def index():
    return render_template("index.html")


@routes.route("/doi", methods=["POST"])
def doi_to_bibtex():
    doi = request.form["doi"]
    if doi == "":
        return render_template("index.html", message="Search field empty")
    doi_data = doi_service.get_doi_data(doi)
    return render_template("index.html", **doi_data)


# lukee formin tiedot
@routes.route("/createbook", methods=["POST"])
def create_book():
    if request.method == "POST":
        book_required_fields = ["acronym", "author", "publisher", "title", "year"]
        all_fields = check_field(request.form, book_required_fields)
        if all_fields:
            clf = remove_whitespace(request.form)
            msg = cite_service.add_book(
                acronym=clf["acronym"],
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
            "acronym",
            "author",
            "journal",
            "title",
            "year",
        ]

        all_fields = check_field(request.form, article_required_fields)
        if all_fields:
            clf = remove_whitespace(request.form)
            msg = cite_service.add_article(
                acronym=clf["acronym"],
                author=clf["author"],
                journal=clf["journal"],
                title=clf["title"],
                year=clf["year"],
                volume=clf["volume"],  # opt
                pages=clf["pages"],  # opt
            )
        else:
            msg = MISSING_FIELD
        return render_template("index.html", message=msg)


@routes.route("/createinproceedings", methods=["POST"])
def create_inproceedings():
    if request.method == "POST":
        inproc_required_fields = ["acronym", "author", "booktitle", "title", "year"]

        all_fields = check_field(request.form, inproc_required_fields)
        if all_fields:
            clf = remove_whitespace(request.form)
            msg = cite_service.add_inproceedings(
                acronym=clf["acronym"],
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

    elif source_type == "article":
        return render_template("index.html", article=True)

    elif source_type == "in_proceedings":
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
            all=True,
        )

@routes.route("/download_bib", methods=["POST"])
def bibload():
    file_path = cite_service.all_bibtex_out()

    return send_file(file_path, as_attachment=True, download_name="references.bib")

def check_field(form: dict, check_list: list):
    for att in check_list:
        if form[att] == "":
            return False
    return True


def remove_whitespace(form: dict):
    clean_form = {key: value.strip() for key, value in form.items()}
    return clean_form
