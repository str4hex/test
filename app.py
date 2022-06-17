from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app1 = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "SQLITE:///db.db"

app1.config["SQLALCHEMY_DATABASE_URI"] = "SQLITE:///db1.db"

db = SQLAlchemy(app)

db1 = SQLAlchemy(app1)
