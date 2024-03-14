import os.path
from os import environ
from flask import Flask

DEBUG = True
DATABASE = '/tmp/db.sqlite3'
SECRET_KEY = str(environ.get("SECRET_KEY"))

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'db.sqlite3')))
