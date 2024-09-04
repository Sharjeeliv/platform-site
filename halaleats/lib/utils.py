# Standard Imports
import os
import secrets

# Third-party Imports
from PIL import Image
from flask import current_app, flash


def save_picture(form_picture):
    # Rename ---------------------
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static', 'certificates', picture_fn)
    # Resize ---------------------
    # output_size = (125, 125)
    i = Image.open(form_picture)
    # i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

def flash_form_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(f'{field.capitalize()}: {error}', category='danger')