from app import app, mysql
from werkzeug.security import generate_password_hash, check_password_hash


class Students(object):

    def __init__(self, firstName=None, lastName=None, gender=None, idNum=None, course=None):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.idNum = idNum
        self.course = course

    def add(self):
        cur = mysql.connection.cursor()
        course = Course()
        course.course_name = self.course
        course_id = course.get_course_id()
        sql = "INSERT INTO students_po2(first_name, last_name, gender, id_number, course_id) \
                VALUES('%s', '%s', '%s', '%s', '%s')" % \
            (self.firstName, self.lastName, self.gender, self.idNum, course_id)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def delete(self):
        cur = mysql.connection.cursor()

        sql = "DELETE FROM students_po2 WHERE id_number = '%s'" % (self.idNum)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def exist(self):
        cur = mysql.connection.cursor()

        sql = "SELECT id_number FROM students_po2 where id_number = '%s'" % (
            self.idNum)
        cur.execute(sql)
        if cur.fetchall():
            cur.close()
            return True
        else:
            cur.close()
            return False

    def update(self, first_name, last_name, gen, id_num, course):
        cur = mysql.connection.cursor()
        try:
            c = Course()
            c.course_name = course
            course_id = c.get_course_id()
            sql = "UPDATE students_po2 SET first_name = '%s', last_name = '%s', gender = '%s', id_number = '%s', course_id = '%s' \
                WHERE id_number = '%s'" % (
                first_name, last_name, gen, id_num, course_id, self.idNum)
            cur.execute(sql)
            mysql.connection.commit()
            cur.close
            return True
        except:
            return False

    @classmethod
    def all(cls):
        cur = mysql.connection.cursor()

        sql = """SELECT students_po2.first_name, students_po2.last_name, students_po2.gender, students_po2.id_number, courses_po2.course_name 
              FROM students_po2, courses_po2
              WHERE students_po2.course_id = courses_po2.course_id"""
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        return result

    @staticmethod
    def search(category, search):
        cur = mysql.connection.cursor()
        if category == 'course':
            sql = f"""SELECT students_po2.first_name, students_po2.last_name, students_po2.gender, students_po2.id_number, courses_po2.course_name 
                 FROM students_po2, courses_po2
                 WHERE (courses_po2.course_title LIKE '{search}%' OR courses_po2.course_name LIKE '{search}%') AND students_po2.course_id = courses_po2.course_id"""
        else:
            sql = """SELECT students_po2.first_name, students_po2.last_name, students_po2.gender, students_po2.id_number, courses_po2.course_name 
                 FROM students_po2, courses_po2
                 WHERE students_po2.{} LIKE '{}%' AND students_po2.course_id = courses_po2.course_id""".format(
                category, search)
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        if result:
            return result
        else:
            return False


class Course(object):
    def __init__(self, course_title=None, course_name=None, id=None):
        self.course_title = course_title
        self.course_name = course_name
        self.id = id

    def get_course_id(self):
        cur = mysql.connection.cursor()
        sql = f"""SELECT course_id
            FROM courses_po2
            WHERE course_title = '{self.course_title}' OR course_name = '{self.course_name}'
            """
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        for r in result:
            return r[0]

    def add_course(self):
        cur = mysql.connection.cursor()
        sql = f"""INSERT INTO courses_po2 (course_name,course_title)
             VALUES ('{self.course_name}', '{self.course_title}')"""
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def course_has_student(self):
        cur = mysql.connection.cursor()
        sql = f"""SELECT students_po2.first_name, students_po2.last_name, students_po2.gender, students_po2.id_number, courses_po2.course_name 
              FROM students_po2, courses_po2
              WHERE courses_po2.course_id = '{self.id}' AND students_po2.course_id = courses_po2.course_id"""
        cur.execute(sql)
        result = cur.fetchall()
        cur.close
        if result:
            return True
        else:
            return False

    @staticmethod
    def delete(id):
        cur = mysql.connection.cursor()
        sql = f"DELETE FROM courses_po2 WHERE course_id = '{id}'"
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    @classmethod
    def all(cls):
        cur = mysql.connection.cursor()
        sql = """
            SELECT *
            FROM courses_po2
        """
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        return result

    def title_exist(self):
        cur = mysql.connection.cursor()
        sql = f"""SELECT *
            FROM courses_po2
            WHERE course_title = '{self.course_title}'
            """
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        if result:
            return True
        else:
            return False

    def name_exist(self):
        cur = mysql.connection.cursor()
        sql = f"""SELECT *
            FROM courses_po2
            WHERE course_name = '{self.course_name}'
            """
        cur.execute(sql)
        result = cur.fetchall()
        print(self.course_name)
        cur.close()
        if result:
            return True
        else:
            return False
