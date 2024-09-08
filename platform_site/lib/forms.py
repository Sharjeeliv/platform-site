# Third-party Imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional

# Local Imports
from platform_site.models import User
from platform_site.lib.const import LANGUAGES, TYPES

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
languages = [(key, value) for key, value in LANGUAGES.items()]
types = [(key, value) for key, value in TYPES.items()]

class ProjectForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=32)])
    description = StringField('Description', validators=[DataRequired(), Length(min=2, max=256)])
    github = StringField('Github Repository', validators=[Optional()])
    link = StringField('Project Link', validators=[Optional()])

    main_lang = SelectField('Main Language', choices=languages, validators=[DataRequired()])
    proj_type = SelectField('Project Type', choices=types, validators=[DataRequired()])
    langtools = StringField('Language & Tools', validators=[Length(min=0, max=256)])

    submit = SubmitField('Submit')


# *********************
# SITE FORMS
# *********************
class SearchForm(FlaskForm):
    main_lang = SelectField('Main Language', choices=languages, validators=[Optional()])
    proj_type = SelectField('Project Type', choices=types, validators=[Optional()])
    submit = SubmitField('→')