import os.path
from flask import Flask

DEBUG = True
DATABASE = '/tmp/db.sqlite3'
SECRET_KEY = os.environ.get("SECRET_KEY", "default_secret_key")

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'db.sqlite3')))
