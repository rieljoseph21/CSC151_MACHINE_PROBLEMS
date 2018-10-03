from app import app, mysql


class Students(object):

    def __init__(self, firstName=None, lastName=None, gender=None, idNum=None, course=None):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.idNum = idNum
        self.course = course

    def add(self):
        cur = mysql.connection.cursor()

        sql = "INSERT INTO students(firstName, lastName, gender, idNum, course) \
                VALUES('%s', '%s', '%s', '%s', '%s')" % \
            (self.firstName, self.lastName, self.gender, self.idNum, self.course)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def delete(self):
        cur = mysql.connection.cursor()

        sql = "DELETE FROM students WHERE idNum = '%s'" % (self.idNum)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close

    def exist(self):
        cur = mysql.connection.cursor()

        sql = "SELECT idNum FROM students where idNum = '%s'" % (self.idNum)
        cur.execute(sql)
        if cur.fetchall():
            cur.close()
            return True
        else:
            cur.close()
            return False

    def update(self, first_name, last_name, gen, id_num, cour):
        cur = mysql.connection.cursor()
        try:
            sql = "UPDATE students SET firstName = '%s', lastName = '%s', gender = '%s', idNum = '%s', course = '%s' WHERE idNum = '%s'" % (
                first_name, last_name, gen, id_num, cour, self.idNum)
            cur.execute(sql)
            mysql.connection.commit()
            cur.close
            return True
        except:
            return False

    @classmethod
    def all(cls):
        cur = mysql.connection.cursor()

        sql = "SElECT * FROM students"
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        return result

    @staticmethod
    def search(category, search):
        cur = mysql.connection.cursor()

        sql = "SELECT * FROM students WHERE %s LIKE '%s'" % (
            category, search)
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        if result:
            return result
        else:
            return False
