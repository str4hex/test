from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app1 = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "SQLITE:///db.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app1.config["SQLALCHEMY_DATABASE_URI"] = "SQLITE:///db1.db"
app1.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

db1 = SQLAlchemy(app1)

@app.route("/")
def page_index():
    return "app1"

@app1.route("/")
def page_index():
    return "app2"


app.run(port=5000)

app1.run(port=5001)
