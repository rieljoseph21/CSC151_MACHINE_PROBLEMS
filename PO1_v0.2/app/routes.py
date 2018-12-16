from flask import render_template, request, flash, redirect, url_for

from app import app
from app.forms import AddStudentForm
from app.models import Student_Profile


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = AddStudentForm()
    if form.validate_on_submit():
        last_name = form.last_name.data.title
        first_name = form.first_name.data.title
        gender = form.gender.data
        id_number = form.id_number.data
        course = form.course.data
        if Student_Profile().student_exist(id_number):
            flash('Student Already Exist in our Master List.')
            redirect(url_for('add_student'))
        else:
            Student_Profile().add_student(
                last_name, first_name, gender, id_number, course)
            flash('Student Added Successfully.')
            redirect(url_for('add_student'))
    return render_template('add_student.html', title='Add', form=form)
