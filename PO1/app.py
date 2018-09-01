from flask import Flask, render_template, request, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, AnyOf

import csv

from student import Student_Profile

app = Flask(__name__)
app.config['SECRET_KEY'] = 'moymoy213'

bootstrap = Bootstrap(app)


class StudentForm(FlaskForm):
    firstname = StringField('First Name ', validators=[DataRequired()])
    lastname = StringField('Last Name ', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[
                         ('M', 'Male'), ('F', 'Female')], default=None, validators=[DataRequired()])
    id_number = StringField('ID Number  ', validators=[DataRequired()])
    course = StringField('Course ', validators=[DataRequired()])
    submit = SubmitField('Add Student')


class DeleteForm(FlaskForm):
    id_number = StringField('ID Number: ', validators=[DataRequired()])
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
