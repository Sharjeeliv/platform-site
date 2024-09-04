# Third-party Imports
from flask import Blueprint, render_template, request, send_from_directory
from flask_login import login_required, current_user
from halaleats.lib.utils import flash_form_errors
from halaleats.models import Eatery
from sqlalchemy import or_

# Local Imports
from halaleats.lib.forms import SearchForm
from halaleats.models import Eatery


main = Blueprint('routes/main', __name__)

@main.route("/about")
def about():
    return render_template('about.html', title='About', user=current_user)

@main.route('/resume')
def resume():
    return send_from_directory('static', 'resume.pdf')

@main.route("/")
def home():
    return render_template('home.html', title='Home', user=current_user)

@main.route("/list", methods=['GET', 'POST'])
def list():    
    # Show search filtered page
    form=SearchForm()
    if form.validate_on_submit():
        """
        A partial implementation of search, will be expanded with search engine
        Distance will also be added in a later addition
        """

        field_mapping = {
        'search': (or_(Eatery.name.ilike(f"%{form.search.data}%"), 
                       Eatery.name.ilike(f"%{form.search.data}%"))),
        'cuisine': (Eatery.cuisine.ilike(f"%{form.cuisine.data}%")),
        'verification': (Eatery.verification_type == form.verification.data)
        }
        filters = {k: v for k, v in field_mapping.items() if form[k].data is not None}
        query = Eatery.query.filter(*filters.values())


        page = request.args.get('page', 1, type=int)
        eateries = query.order_by(Eatery.name.desc()).paginate(page=page, per_page=5)
        return render_template('projects.html', form=form, eateries=eateries, user=current_user)

    else:
        flash_form_errors(form)

    # Show default page
    page = request.args.get('page', 1, type=int)
    eateries = Eatery.query.order_by(Eatery.name.desc()).paginate(page=page, per_page=5)
    return render_template('projects.html', form=form, eateries=eateries, title='Home', user=current_user)

    

