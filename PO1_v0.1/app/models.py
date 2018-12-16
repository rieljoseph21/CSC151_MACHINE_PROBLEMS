import csv
from os import path


class Student_Profile(object):
    path = path.abspath('database.txt')

    def display_students(self):
        rows = []
        with open(self.path, 'r', newline='') as f_in:
            reader = csv.reader(f_in, delimiter=',')
            for row in reader:
                rows.append(row)
        return rows

    def add_students(self, lastname, firstname, gender, id_number, course):
        with open(self.path, 'a', newline='') as f_in:
            added_row = [lastname, firstname, gender, id_number, course]
            f_in.write(','.join(added_row) + '\n')
        self.sort_students()

    def sort_students(self):
        old_rows = []
        with open(self.path, 'r', newline='') as f_in:
            reader = csv.reader(f_in)
            header = next(reader)
            for row in reader:
                old_rows.append(row)
        new_rows = sorted(old_rows, key=lambda row: row[0])
        with open(self.path, 'w', newline='') as f_out:
            f_out.write(','.join(header) + '\n')
            for row in new_rows:
                f_out.write(','.join(row) + '\n')

    def delete_students(self, id_number):
        old_rows = []
        with open(self.path, 'r', newline='') as f_in:
            reader = csv.reader(f_in)
            for row in reader:
                old_rows.append(row)
        with open(self.path, 'w', newline='') as f_out:
            for row in old_rows:
                if row[3] != id_number:
                    f_out.write(','.join(row) + '\n')

    def student_exist(self, id_number):
        with open(self.path, 'r', newline='') as f_in:
            reader = csv.reader(f_in)
            header = next(reader)
            for row in reader:
                if row[3] == id_number:
                    return True
        return False


if __name__ == '__main__':
    st = Student_Profile()
    print(st.display_students())
