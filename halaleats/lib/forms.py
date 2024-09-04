# Third-party Imports
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional

# Local Imports
from halaleats.models import User
from halaleats.lib.const import CUISINES, VERIFICATIONS, DISTANCES, ALCOHOL_SERVICE

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
# EATERY FORM
# *********************
class EateryForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=100)])
    picture = FileField('Certificate', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    cuisine = SelectField('Cuisine', choices=CUISINES)
    verification = SelectField('Verification', choices=VERIFICATIONS)
    alcohol_service = SelectField('Alcohol', choices=ALCOHOL_SERVICE)
    submit = SubmitField('Submit')


# *********************
# SITE FORMS
# *********************
class SearchForm(FlaskForm):
    search = StringField('Search', validators=[Length(max=200)])
    cuisine = SelectField('Cuisine', choices=CUISINES, validators=[Optional()])
    verification = SelectField('Verification', choices=VERIFICATIONS, validators=[Optional()])
    distance = SelectField('Distance', choices=DISTANCES, validators=[Optional()])
    submit = SubmitField('→')