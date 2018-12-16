from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Regexp, ValidationError, AnyOf, EqualTo, Email

from app import mysql
from app.models import Students, Course


class StudentForm(FlaskForm):
    # Form for adding student.
    firstname = StringField('First Name ', validators=[DataRequired(),
                                                       Regexp('^[A-Za-z ]{2,30}$', message="Enter a valid First name.")])
    lastname = StringField('Last Name ', validators=[DataRequired(),
                                                     Regexp('^[A-Za-z ]{2,15}$', message="Enter a valid Last name.")])
    gender = SelectField('Gender', choices=[('', '<--- choose option --->'),
                                            ('M', 'Male'), ('F', 'Female')], validators=[AnyOf(('M', 'F'), message=u"Please choose your Gender")])
    id_number = StringField('ID Number  ', validators=[DataRequired(), Regexp(
        '^[0-9]{4}\-[0-9]{4}$', message="Please enter a valid id number, Example: 2014-1716")])
    course_id = StringField('Course Title', validators=[DataRequired(), Regexp(
        '^[A-Z]{2,3}\-[A-Za-z]{2,5}$', message="Please enter a valid course, or look through our course list Example: BS-CS")])
    submit = SubmitField('Execute')

    def validate_id_number(self, id_number):
        user = Students()
        user.idNum = id_number.data
        if user.exist():
            raise ValidationError('ID Number Already Used!')

    def validate_course_id(self, course_id):
        course = Course()
        course.course_name = course_id.data
        if course.name_exist() is False:
            raise ValidationError(
                'Course Title not Found! please add the course or check what the course list')


class EditStudentForm(FlaskForm):
    # Form for adding student.
    firstname = StringField('First Name ', validators=[DataRequired(),
                                                       Regexp('^[A-Za-z ]{2,30}$', message="Enter a valid First name.")])
    lastname = StringField('Last Name ', validators=[DataRequired(),
                                                     Regexp('^[A-Za-z ]{2,15}$', message="Enter a valid Last name.")])
    gender = SelectField('Gender', choices=[('', '<--- choose option --->'),
                                            ('M', 'Male'), ('F', 'Female')], validators=[AnyOf(('M', 'F'), message=u"Please choose your Gender")])
    id_number = StringField('ID Number  ', validators=[DataRequired(), Regexp(
        '^[0-9]{4}\-[0-9]{4}$', message="Please enter a valid id number, Example: 2014-1716")])
    course_id = StringField('Course Title', validators=[DataRequired(), Regexp(
        '^[A-Z]{2,3}\-[A-Za-z]{2,5}$', message="Please enter a valid course, or look through our course list Example: BS-CS")])
    submit = SubmitField('Execute')

    def validate_course_id(self, course_id):
        course = Course()
        course.course_name = course_id.data
        if course.name_exist() is False:
            raise ValidationError(
                'Course Title not Found! please add the course or check what the course list')


class CourseForm(FlaskForm):
    course_title = StringField('Course Title', validators=[DataRequired()])
    course_name = StringField('Course Abbreviation',
                              validators=[DataRequired(), Regexp(
                                  '^[A-Z]{2,3}\-[A-Za-z]{2,5}$', message="Please enter a valid course Abbreviation, Example: BS-CS")])
    submit = SubmitField('Add')

    def validate_course_title(self, course_title):
        course = Course()
        course.course_title = course_title.data
        if course.title_exist():
            raise ValidationError('Course Title Already Exist!')

    def validate_course_name(self, course_name):
        course = Course()
        course.course_name = course_name.data
        if course.name_exist():
            raise ValidationError('Course Name Already Exist!')


class DeleteForm(FlaskForm):
    # Form for deleting student.
    id_number = StringField('ID Number ', validators=[Regexp(
        '^[0-9]{4}\-[0-9]{4}$', message="Please enter a valid id number, Example: 2014-1716")])
    submit = SubmitField('Delete')


class SearchForm(FlaskForm):
    # Form for searching student.
    search = StringField('Search Students', validators=[
                         DataRequired(message='Field Required.')])
    choice = SelectField('Filter by', choices=[('', 'Category'),
                                               ('first_name', 'First Name'),
                                               ('last_name', 'Last Name'),
                                               ('id_number', 'ID #'),
                                               ('course', 'Course'),
                                               ('gender', 'Gender')
                                               ], validators=[AnyOf(('first_name', 'last_name', 'id_number', 'course', 'gender'), message=u'Select Category to search.')])
    submit = SubmitField('Search')
