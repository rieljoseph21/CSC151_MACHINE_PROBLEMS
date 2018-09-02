from flask import Flask, render_template, request, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Regexp

import csv

from student import Student_Profile

app = Flask(__name__)

# Required for using wtforms
app.config['SECRET_KEY'] = 'moymoy213'

# Extension for using Bootstrap's stylsheet
bootstrap = Bootstrap(app)

# Form for adding studnet.


class StudentForm(FlaskForm):
    firstname = StringField('First Name ', validators=[
                            Regexp('^[A-Za-z ]{2,30}$', message="Enter a valid First name.")])
    lastname = StringField('Last Name ', validators=[
        Regexp('^[A-Za-z ]{2,15}$', message="Enter a valid Last name.")])
    gender = SelectField('Gender', choices=[
                         ('M', 'Male'), ('F', 'Female')], default=None, validators=[DataRequired()])
    id_number = StringField('ID Number  ', validators=[Regexp(
        '^[0-9]{4}\-[0-9]{4}$', message="Please enter a valid id number, Example: 2014-1716")])
    course = StringField('Course ', validators=[Regexp(
        '^[A-Z]{2,3}\-[A-Z]{2,5}$', message="Please enter a valid course, Example: BS-CS")])
    submit = SubmitField('Add Student')


class DeleteForm(FlaskForm):
    id_number = StringField('ID Number: ', validators=[Regexp(
        '^[0-9]{4}\-[0-9]{4}$', message="Please enter a valid id number, Example: 2014-1716")])
    submit = SubmitField('Delete')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/students')
def students():
    rows = []
    with open('database.csv') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            rows.append(row)

    return render_template('students.html', header=header, rows=rows)


@app.route('/delete_student', methods=['GET', 'POST'])
def delete_student():
    form = DeleteForm()
    if request.method == 'POST' and form.validate():
        Student_Profile().delete_student(form.id_number.data)
        return redirect(url_for('students'))
    return render_template('delete_student.html', form=form)


@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if request.method == 'POST' and form.validate():
        Student_Profile().add_student(form.firstname.data, form.lastname.data,
                                      form.gender.data, form.id_number.data, form.course.data)
        return redirect(url_for('students'))
    return render_template('add_student.html', form=form)
