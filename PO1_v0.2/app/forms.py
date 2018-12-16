from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Regexp, AnyOf

from app.models import Student_Profile


class AddStudentForm(FlaskForm):
    name_regexp = '^[a-zA-Z ]{2,15}$'
    name_message = 'Please input a valid name.'
    last_name = StringField('Last Name', validators=[
                            DataRequired(), Regexp('^[a-zA-Z ]{2,15}$', message='Please input a valid name.')])
    first_name = StringField('First Name', validators=[
                             DataRequired(), Regexp('^[a-zA-Z ]{2,15}$', message='Please input a valid name.')])
    gender = SelectField(
        'Gender',
        choices=[('', '<--- Choose Gender --->'),
                 ('M', 'Male'), ('F', 'Female')],
        validators=[AnyOf(('M', 'F'), message='Please choose your gender.')])
    id_number = StringField(
        'ID number',
        validators=[
            DataRequired(),
            Regexp('^[0-9]{4}\-[0-9]{4}$',
                   message='Please Input a valid ID Number. Example: 2014-1716')
        ])
    course = StringField(
        'Course',
        validators=[
            DataRequired(),
            Regexp('^[A-Z]{2,4}\-[A-Z]{2,5}$',
                   message='Please Input a valid Course. Example: BS-CS')
        ])
    submit = SubmitField('Add')
