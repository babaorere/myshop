import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.abspath(os.getcwd()) + "/myshop.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "lknmvfsdok394805·$%$·%&"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from shop.admin import routes
