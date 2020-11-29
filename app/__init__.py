from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db_config import config

app = Flask(__name__)
db_url = 'mysql://' + config['MYSQL_USER'] + ':' + config['MYSQL_PASSWORD'] + '@' + config['MYSQL_HOST'] + '/' + config['MYSQL_DB']
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

db = SQLAlchemy(app)
db.create_all()

from app.service import user_service