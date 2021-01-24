from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db_config import config
from flask_cors import CORS

PROFILE_SERVICE_URL  = 'https://praxisreport-profilemanagement.azurewebsites.net/'

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
db_url = 'mysql://' + config['MYSQL_USER'] + ':' + config['MYSQL_PASSWORD'] + '@' + config['MYSQL_HOST'] + ':' + config['MYSQL_PORT'] + '/' + config['MYSQL_DB']
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

db = SQLAlchemy(app)

from app.service import user_service
from app.domain.user import *

db.create_all()

