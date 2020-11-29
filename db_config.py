# from app import app
from flask_mysqldb import MySQL
import os
config = {}

config['MYSQL_HOST'] = 'remotemysql.com'
config['MYSQL_USER'] = 'LtwRz4Bmyp'
config['MYSQL_PASSWORD'] = 'DhzfFPkNEt'
config['MYSQL_DB'] = 'LtwRz4Bmyp'
config['MYSQL_CURSORCLASS'] = 'DictCursor'