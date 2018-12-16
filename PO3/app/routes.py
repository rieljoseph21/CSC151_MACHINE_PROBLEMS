from app import app
from flask import render_template, redirect, url_for, request, flash
from app.models import Students, Course
from app.forms import StudentForm, DeleteForm, SearchForm, CourseForm, EditStudentForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_student', methods=['GET', 'POST'])
# Page for adding student
def add_student():
    form = StudentForm()
    if request.method == 'POST' and form.validate_on_submit():
        student = Students(form.firstname.data.title(), form.lastname.data.title(),
                           form.gender.data, form.id_number.data, form.course_id.data)
        if student.exist() is False:
            student.add()
            flash("Student Added Successfully with ID number '{}'".format(
                form.id_number.data), category='success')
            return redirect(url_for('students'))
        else:
            flash("Student Already Exist!", category='danger')
            return redirect(url_for('add_student'))
    else:
        return render_template('add_student.html', form=form)


@app.route('/studentlist', methods=['GET', 'POST'])
# Page for listing Students.
def students():
    form = SearchForm()
    if request.method == 'POST' and form.validate():
        filteredStudents = Students.search(form.choice.data, form.search.data)
        students = filteredStudents
        return render_template('display_students.html', form=form, filtered=students, students="")
    else:
        students = Students.all()
        return render_template('display_students.html', form=form, students=students, filtered="")


@app.route('/edit/<student_id>', methods=['POST', 'GET'])
def edit_student(student_id):
    form = EditStudentForm()
    db = Students(idNum=student_id)
    student = db.search('id_number', student_id)
    if request.method == 'POST' and form.validate_on_submit():
        newId = Students(idNum=form.id_number.data)
        if(newId.exist() and student_id != form.id_number.data):
            flash('ID number already taken please choose another ID NUMBER',
                  category='danger')
            return redirect(url_for('edit_student', student_id=student_id))
        else:
            db.update(form.firstname.data, form.lastname.data,
                      form.gender.data, form.id_number.data, form.course_id.data)
            flash('Successfully Edited Student', category='success')
            return redirect(url_for('students'))
    else:
        for attribute in student:
            form.firstname.data = attribute[0]
            form.lastname.data = attribute[1]
            form.gender.data = attribute[2]
            form.id_number.data = attribute[3]
            form.course_id.data = attribute[4]
        return render_template('edit_student.html', form=form)


@app.route('/delete/<student_id>', methods=['GET', 'POST'])
def delete(student_id):
    student = Students(idNum=student_id)
    student.delete()
    flash(f"Deleted student with id number '{student_id}'", category='success')
    return redirect(url_for('students'))


@app.route('/delete_student', methods=['GET', 'POST'])
def delete_student():
    form = DeleteForm()
    if request.method == 'POST' and form.validate():
        student = Students(idNum=form.id_number.data)
        if student.exist():
            student.delete()
            flash("Deleted student with id number '{}'".format(
                form.id_number.data), category='success')
            return redirect(url_for('students'))
        else:
            flash("Student Does not exist.", category='danger')
            return redirect(url_for('delete_student'))
    else:
        return render_template('delete_student.html', form=form)


@app.route('/delete_course/<id>')
def delete_course(id):
    course = Course()
    course.id = id
    if course.course_has_student():
        flash('Course Has a Student Enrolled in it. Please Update the student\'s course to delete the specified course.', category='danger')
        return redirect(url_for('students'))
    else:
        course.delete(id)
        flash('Successfully Deleted Course!', category='success')
        return redirect(url_for('courses'))


@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    form = CourseForm()
    course = Course()
    if request.method == 'POST' and form.validate_on_submit():
        course.course_title = form.course_title.data
        course.course_name = form.course_name.data
        course.add_course()
        flash(
            f'Successfully Added course of title "{form.course_title.data}"', category='success')
        return redirect(url_for('courses'))
    else:
        return render_template('add_course.html', form=form)


@app.route('/courselist')
def courses():
    course = Course.all()
    return render_template('display_courses.html', courses=course)
