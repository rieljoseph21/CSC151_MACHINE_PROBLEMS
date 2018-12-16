from flask import Flask
from flask_mysqldb import MySQL
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY

app = Flask(__name__)


mysql = MySQL()

app.config['MYSQL_USER'] = DB_USERNAME
app.config['MYSQL_PASSWORD'] = DB_PASSWORD
app.config['MYSQL_DB'] = DB_NAME
app.config['MYSQL_HOST'] = DB_HOST
app.config['SECRET_KEY'] = SECRET_KEY

mysql.init_app(app)

from app import controller
