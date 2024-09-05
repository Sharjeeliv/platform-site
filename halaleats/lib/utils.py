# Third-party Imports
from flask import current_app, flash

def flash_form_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(f'{field.capitalize()}: {error}', category='danger')