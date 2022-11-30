from db import db
from app import create_app

app = create_app()
app.app_context().push()


def create_tables():
    db.session.execute(
        """
            CREATE TABLE books (
            id SERIAL PRIMARY KEY,
            author TEXT,
            title TEXT,
            year INTEGER,
            publisher TEXT
        );
    """
    )

    db.session.commit()


def drop_tables():
    db.session.execute(
        """
        DROP TABLE IF EXISTS books;
    """
    )

    db.session.commit()


def initialize_database():
    drop_tables()
    create_tables()


if __name__ == "__main__":
    initialize_database()
