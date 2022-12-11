from db import db
from app import create_app

app = create_app()
app.app_context().push()


def create_table():
    db.session.execute(
        """
            CREATE TABLE cites (
            id SERIAL PRIMARY KEY,
            acronym TEXT,
            type TEXT,
            title TEXT,
            author TEXT,
            year INTEGER,
            publisher TEXT,
            volume INTEGER,
            booktitle TEXT,
            journal TEXT,
            pages TEXT,
            bibitex TEXT
        );
    """
    )

    db.session.commit()


def drop_table():
    db.session.execute(
        """
        DROP TABLE IF EXISTS cites;
    """
    )

    db.session.commit()


def initialize_database():
    drop_table()
    create_table()


if __name__ == "__main__":
    initialize_database()
