# Third-party Imports
from os import link
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional

# Local Imports
from halaleats.models import User
from halaleats.lib.const import LANGUAGES, TYPES

# *********************
# USER FORMS
# *********************
class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    token = PasswordField('Token', validators=[DataRequired()])
    submit = SubmitField('Submit')

    @staticmethod
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')
        

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


# *********************
# PROJECT FORM
# *********************
class ProjectForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    description = StringField('Description', validators=[DataRequired(), Length(min=2, max=100)])
    github = StringField('Github Repository')
    link = StringField('Project Link')

    main_lang = SelectField('Main Language', choices=LANGUAGES, validators=[DataRequired()])
    proj_type = SelectField('Project Type', choices=TYPES, validators=[DataRequired()])
    langtools = StringField('Language & Tools', validators=[Length(min=0, max=100)])

    submit = SubmitField('Submit')


# *********************
# SITE FORMS
# *********************
class SearchForm(FlaskForm):
    main_lang = SelectField('Main Language', choices=LANGUAGES, validators=[Optional()])
    proj_type = SelectField('Project Type', choices=TYPES, validators=[Optional()])
    submit = SubmitField('→')