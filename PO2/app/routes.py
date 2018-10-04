from app import app
from flask import render_template, redirect, url_for, request, flash
from app.models import Students
from app.forms import StudentForm, DeleteForm, SearchForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_student', methods=['GET', 'POST'])
# Page for adding student
def add_student():
    form = StudentForm()
    if request.method == 'POST' and form.validate():
        student = Students(form.firstname.data, form.lastname.data,
                           form.gender.data, form.id_number.data, form.course.data)
        if student.exist() is False:
            student.add()
            flash("Student Added Successfully with ID number '{}'".format(
                form.id_number.data))
            return redirect(url_for('students'))
        else:
            flash("Student Already Exist!")
            return redirect(url_for('add_student'))
    else:
        return render_template('add_student.html', form=form)


@app.route('/masterlist', methods=['GET', 'POST'])
def students():
    form = SearchForm()
    if request.method == 'POST' and form.validate():
        filteredStudents = Students.search(form.choice.data, form.search.data)
        students = filteredStudents
        if filteredStudents is False:
            flash('Search Error! "{}" does not exist on our list or you have the wrong category'.format(
                form.search.data))
            return redirect(url_for('students'))
        return render_template('display_students.html', form=form, filtered=students, students="")
    else:
        students = Students.all()
        return render_template('display_students.html', form=form, students=students, filtered="")


@app.route('/edit/<student_id>', methods=['POST', 'GET'])
def edit_student(student_id):
    form = StudentForm()
    db = Students(idNum=student_id)
    student = db.search('idNum', student_id)
    if request.method == 'POST' and form.validate():
        newId = Students(idNum=form.id_number.data)
        if(newId.exist()):
            flash('ID number already taken please choose another ID NUMBER')
            return redirect(url_for('edit_student', student_id=db.idNum))
        else:
            db.update(form.firstname.data, form.lastname.data,
                      form.gender.data, form.id_number.data, form.course.data)
            flash('Successfully Edited Student')
            return redirect(url_for('students'))
    else:
        for attribute in student:
            form.firstname.data = attribute[0]
            form.lastname.data = attribute[1]
            form.gender.data = attribute[2]
            form.id_number.data = attribute[3]
            form.course.data = attribute[4]
        return render_template('edit_student.html', form=form)


@app.route('/delete_student', methods=['GET', 'POST'])
def delete_student():
    form = DeleteForm()
    if request.method == 'POST' and form.validate():
        student = Students(idNum=form.id_number.data)
        if student.exist():
            student.delete()
            flash("Deleted student with id number '{}'".format(form.id_number.data))
            return redirect(url_for('students'))
        else:
            flash("Student Does not exist.")
            return redirect(url_for('delete_student'))
    else:
        return render_template('delete_student.html', form=form)
