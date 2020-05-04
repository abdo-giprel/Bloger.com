from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '6dc87ef97b330819078b05a81754c06c'

db=SQLAlchemy(app)

from blogger import routes