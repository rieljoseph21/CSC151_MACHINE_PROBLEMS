from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Regexp, AnyOf, ValidationError
from app.models import Student_Profile


class AddForm(FlaskForm):
    lastname = StringField(
        'Last Name', validators=[
            DataRequired(), Regexp('^[a-zA-Z ]{2,30}$', message='Input a Valid name')])
    firstname = StringField(
        'First Name', validators=[
            DataRequired(), Regexp('^[a-zA-Z ]{2,30}$', message='Input a valid name')])
    gender = SelectField(
        'Gender', choices=[
            ('', '<-- Option -->'), ('M', 'Male'), ('F', 'Female')],
        validators=[AnyOf(('M', 'F'), message='Please choose your Gender.')])
    id_number = StringField('ID number', validators=[DataRequired(), Regexp(
        '^[0-9]{4}\-[0-9]{4}$',
        message='Please enter a valid id-number, Example: 2014-1716')])
    course = StringField(
        'Course',
        validators=[DataRequired(),
                    Regexp('^[A-Z]{2,4}\-[A-Z]{2,5}$',
                           message='Enter a valid Course, Example: BS-CS')])
    submit = SubmitField('Add')


class DeleteForm(FlaskForm):
    id_number = StringField('ID number', validators=[DataRequired(), Regexp(
        '^[0-9]{4}\-[0-9]{4}$',
        message='Please enter a valid id-number, Example: 2014-1716 ')])
    submit = SubmitField('Delete')
