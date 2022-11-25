from os import getenv
from flask import (
    Flask,
    render_template,
    redirect,
)

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")