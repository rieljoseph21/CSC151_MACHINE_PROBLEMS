import csv
import sys
import os


class Student_Profile():
    filename = 'database.csv'

    def add_student(self, first_name, last_name, gender, id_number, course):
        with open(self.filename, 'a', newline='') as f:
            row = [first_name, last_name, gender, id_number, course]
            f.write(','.join(row) + '\n')

    def delete_student(self, id_number):
        rows = []
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)
        with open(self.filename, 'w') as f:
            for row in rows:
                if row[3] != id_number:
                    f.write(','.join(row) + '\n')

    def display_students(self):
        rows = []
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)
        return rows

    def student_exist(self, id_number):
        with open(self.filename) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if id_number == row[3]:
                    return True
        return False


print(Student_Profile().student_exist('2014-3212'))
