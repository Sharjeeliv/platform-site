# Third-party Imports
from flask import Blueprint,render_template, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user

# Local Imports
from platform import db, bcrypt, signup_token
from platform_site.models import User
from platform_site.lib.forms import RegistrationForm, LoginForm
from platform_site.lib.utils import flash_form_errors


auth = Blueprint('routes/auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash('Logged in', category='success')
            login_user(user, remember=True)
            return redirect(url_for('routes/main.home'))
        flash('Login unsuccessful. Please check your email and password', category='danger')
    else:
        flash_form_errors(form=form)
    return render_template('login.html', title='Login', form=form, user=current_user)

# *********************
@auth.route("/register", methods=['GET', 'POST'])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():

        # Ensure user has signup token
        if form.token.data != signup_token:
            flash('Incorrect Token', 'danger')
            return render_template('register.html', title='Register', form=form, user=current_user)

        # Create a new user and add to database
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            email=form.email.data, 
            first_name=form.first_name.data, 
            last_name=form.last_name.data, 
            password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You can now login', category='success')
        return redirect(url_for('routes/main.home'))
    
    else:
        # Flash form validation errors
        flash_form_errors(form)
    return render_template('register.html', title='Register', form=form, user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes/auth.login'))