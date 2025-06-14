import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['HOST'] = '0.0.0.0'
app.config['PORT']=8000
app.config['DEBUG'] = True

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

db = SQLAlchemy()