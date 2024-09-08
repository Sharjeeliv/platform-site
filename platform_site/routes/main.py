# Third-party Imports
from flask import Blueprint, render_template, request, send_from_directory, url_for
from flask_login import login_required, current_user
from platform_site.lib.utils import flash_form_errors

# Local Imports
from platform_site.lib.forms import SearchForm
from platform_site.models import Project
from platform_site.lib.const import LANGUAGES, TYPES


main = Blueprint('routes/main', __name__)

@main.route("/temp")
def about():
    return render_template('temp.html', user=current_user)

@main.route('/resume')
def resume():
    return send_from_directory('static', 'Resume.pdf')

@main.route("/")
def home():
    return render_template('home.html', title='Home', user=current_user)

@main.route("/projects", methods=['GET', 'POST'])
def projects():    
    # Show search filtered page
    form=SearchForm()
    if form.validate_on_submit():


        field_mapping = {
        'proj_type': (Project.type.ilike(f"%{form.proj_type.data}%")),
        'main_lang': (Project.main == form.main_lang.data)
        }
        filters = {k: v for k, v in field_mapping.items() if form[k].data is not None}
        query = Project.query.filter(*filters.values())

        page = request.args.get('page', 1, type=int)
        projects = query.order_by(Project.name.desc()).paginate(page=page, per_page=5)
        return render_template('projects.html', form=form, projects=projects, user=current_user, langs=LANGUAGES, types=TYPES)

    else:
        flash_form_errors(form)

    # Show default page
    page = request.args.get('page', 1, type=int)
    projects = Project.query.order_by(Project.name.desc()).paginate(page=page, per_page=5)
    return render_template('projects.html', form=form, projects=projects, title='Home', user=current_user, langs=LANGUAGES, types=TYPES)

    

