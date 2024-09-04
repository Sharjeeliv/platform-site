# Local Imports
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

# Local Imports
from halaleats import db
from halaleats.lib.forms import EateryForm
from halaleats.lib.utils import flash_form_errors, save_picture
from halaleats.models import Eatery


eatery = Blueprint('routes/eatery', __name__)


@eatery.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    form = EateryForm()
    print(form.validate_on_submit())
    
    if form.validate_on_submit():
        image_name = save_picture(form.picture.data) if form.picture.data else ""

        eatery = Eatery(
            name=form.name.data,
            address=form.address.data,
            cuisine=form.cuisine.data,
            verification_type=form.verification.data,
            certificate_file=image_name,
            alcohol_served=True if form.alcohol_service.data=='True' else False,
            )
        
        db.session.add(eatery)
        db.session.commit()
        flash(f'Eatery successfuly saved', category='success')
        return redirect(url_for('routes/main.home'))
    else:
        # Flash form validation errors
        flash_form_errors(form)
    return render_template('eatery_input.html', title='Create Eatery', form=form, user=current_user)

@eatery.route("/eatery/<int:eatery_id>/delete", methods=['GET', 'POST'])
@login_required
def delete(eatery_id: int):
    eatery = Eatery.query.get_or_404(eatery_id)
    db.session.delete(eatery)
    db.session.commit()
    flash('Post Deleted', 'success')
    return redirect(url_for('routes/main.home'))

@eatery.route("/eatery/<int:eatery_id>/update", methods=['GET', 'POST'])
@login_required
def update(eatery_id: int):
    eatery = Eatery.query.get_or_404(eatery_id)
    form = EateryForm()

    if form.validate_on_submit():
        eatery.name=form.name.data
        eatery.address=form.address.data
        eatery.cuisine=form.cuisine.data
        eatery.verification_type=form.verification.data
        eatery.alcohol_served=True if form.alcohol_service.data=='True' else False

        if form.picture.data:
            image_name = save_picture(form.picture.data) if form.picture.data else ""
            eatery.certificate_file=image_name

        db.session.commit()
        flash('Post updated', 'success')
        return redirect(url_for('routes/main.home'))
    
    elif request.method == 'GET':
        form.name.data = eatery.name
        form.address.data=eatery.address
        form.cuisine.data=eatery.cuisine
        form.verification.data=eatery.verification_type
        form.alcohol_service.data=eatery.alcohol_served

    return render_template('eatery_input.html', title='Update Eatery', form=form, user=current_user)