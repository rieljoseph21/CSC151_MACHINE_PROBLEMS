import os


class Config(object):
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = os.environ.get('PASSWORD')
    MYSQL_DB = 'student_csc151'
    MYSQL_HOST = 'localhost'
    SECRET_KEY = 'random'
