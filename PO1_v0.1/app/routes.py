from flask import redirect, render_template, request, flash, url_for

from app import app
from app.models import Student_Profile
from app.forms import AddForm, DeleteForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = AddForm()
    if form.validate_on_submit():
        if Student_Profile().student_exist(form.id_number.data):
            flash('Student with id number {} already exist.'.format(
                form.id_number.data))
            redirect(url_for('add_student'))
        else:
            lastname = form.lastname.data.title()
            firstname = form.firstname.data.title()
            gender = form.gender.data
            id_number = form.id_number.data
            course = form.course.data
            Student_Profile().add_students(
                lastname, firstname, gender, id_number, course)
            flash('Student added Successfully!')
            redirect(url_for('add_student'))
    return render_template('add_student.html', form=form, title='Add')


@app.route('/delete_student', methods=['GET', 'POST'])
def delete_student():
    form = DeleteForm()
    if form.validate_on_submit():
        id_number = form.id_number.data
        if Student_Profile().student_exist(id_number):
            Student_Profile().delete_students(id_number)
            flash('Student deleted Successfully!')
            redirect(url_for('delete_student'))
        else:
            flash('Student with id number {} do not exist!'.format(id_number))
            redirect(url_for('delete_student'))
    return render_template('delete_student.html', form=form, title='Delete')


@app.route('/display_students')
def display_students():
    rows = Student_Profile().display_students()
    header = rows.pop(0)
    return render_template('display_students.html',
                           title='Display', rows=rows, header=header)
