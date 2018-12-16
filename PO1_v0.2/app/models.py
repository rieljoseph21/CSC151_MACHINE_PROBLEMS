import os
import csv


class Student_Profile(object):
    filepath = os.path.abspath('database.txt')

    def add_student(self, last_name, first_name, gender, id_number, course):
        new_row = [last_name, first_name, gender, id_number, course]
        with open(self.filepath, 'a', newline='') as f_in:
            f_in.write(','.join(new_row) + '\n')
        self.sort_students()

    def delete_student(self, id_number):
        old_row = []
        with open(self.filepath, 'r', newline='') as f_in:
            reader = csv.reader(f_in)
            for row in reader:
                old_row.append(row)
        with open(self.filepath, 'w', newline='') as f_out:
            for row in old_row:
                if row[3] != id_number:
                    f_out.write(','.join(row) + '\n')
        self.sort_students()

    def display_students(self):
        rows = []
        with open(self.filepath, 'r', newline='') as f_in:
            reader = csv.reader(f_in)
            header = next(reader)
            for row in reader:
                rows.append(row)
        return rows

    def student_exist(self, id_number):
        with open(self.filepath, 'r', newline='') as f_in:
            reader = csv.reader(f_in)
            header = next(reader)
            for row in reader:
                if id_number == row[3]:
                    return True
        return False

    def sort_students(self):
        before_sort = []
        with open(self.filepath, 'r', newline='') as f_in:
            reader = csv.reader(f_in)
            header = next(reader)
            for row in reader:
                before_sort.append(row)
            after_sort = sorted(before_sort, key=lambda row: row[0])
        with open(self.filepath, 'w', newline='') as f_out:
            f_out.write(','.join(header) + '\n')
            for row in after_sort:
                f_out.write(','.join(row) + '\n')


if __name__ == '__main__':
    Student_Profile().sort_students()
