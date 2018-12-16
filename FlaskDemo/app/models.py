from app import app, mysql


class Users(object):

    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email

    def add(self):
        cursor = mysql.connection.cursor()

        sql = "INSERT INTO users(username,password,email) \
                VALUES('%s','%s','%s')" % \
            (self.username, self.password, self.email)

        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from users"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
