import sqlite3
from flask import g
from settings import *


def get_database_connection():
    connect = sqlite3.connect(app.config['DATABASE'])
    connect.row_factory = sqlite3.Row
    return connect


def create_database():
    database = get_database_connection()
    with app.open_resource('models.sql', 'r') as db:
        database.cursor().executescript(db.read())
    database.commit()
    database.close()


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
        with sqlite3.connect('db.sqlite3') as db:
            cur = db.cursor()
            cur.execute(f'SELECT title, content FROM website WHERE url LIKE "{url}" LIMIT 1')
            return cur.fetchall()[0]
    except:
        create_database()
        print('* A new database has been created!')
