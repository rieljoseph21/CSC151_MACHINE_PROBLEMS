from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Regexp, ValidationError, AnyOf


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
    course = StringField('Course ', validators=[DataRequired(), Regexp(
        '^[A-Z]{2,3}\-[A-Za-z]{2,5}$', message="Please enter a valid course, Example: BS-CS")])
    submit = SubmitField('Execute')


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
                                               ('firstName', 'First Name'),
                                               ('lastName', 'Last Name'),
                                               ('idNum', 'ID #'),
                                               ('course', 'Course'),
                                               ('gender', 'Gender')
                                               ], validators=[AnyOf(('firstName', 'lastName', 'idNum', 'course', 'gender'), message=u'Select Category to search.')])
    submit = SubmitField('Search')
