import sqlite3
from flask import g
from settings import app


def get_database_connection():
    connect = sqlite3.connect(app.config['DATABASE'])
    connect.row_factory = sqlite3.Row
    return connect


def create_database():
    with get_database_connection() as database:
        with app.open_resource('models.sql', 'r') as db:
            database.cursor().executescript(db.read())
        database.commit()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = get_database_connection()
    return g.link_db


@app.do_teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


def get_db_objects(url):
    try:
        cur = get_db().cursor()
        cur.execute('SELECT title, content FROM website WHERE url = ? LIMIT 1', (url,))
        return cur.fetchall()[0]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        create_database()
        return None
