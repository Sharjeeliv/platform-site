# Local Imports
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

# Local Imports
from halaleats import db
from halaleats.lib.forms import ProjectForm
from halaleats.lib.utils import flash_form_errors
from halaleats.models import Project


project = Blueprint('routes/project', __name__)


@project.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    form = ProjectForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        project = Project(
            name=form.name.data,
            description=form.description.data,
            github=form.github.data,
            type=form.proj_type.data,
            main=form.main_lang.data,
            langtools=form.langtools.data
            )
        
        db.session.add(project)
        db.session.commit()
        flash(f'Project successfuly saved', category='success')
        return redirect(url_for('routes/main.projects'))
    else:
        # Flash form validation errors
        flash_form_errors(form)
    return render_template('project_input.html', title='Create Project', form=form, user=current_user)

@project.route("/<int:project_id>/delete", methods=['GET', 'POST'])
@login_required
def delete(project_id: int):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    flash('Project Deleted', 'success')
    return redirect(url_for('routes/main.projects'))

@project.route("/<int:project_id>/update", methods=['GET', 'POST'])
@login_required
def update(project_id: int):
    project = Project.query.get_or_404(project_id)
    form = ProjectForm()

    if form.validate_on_submit():
        project.name=form.name.data
        project.description=form.description.data
        project.github=form.github.data
        project.link=form.link.data
        project.type=form.proj_type.data
        project.main=form.main_lang.data
        project.langtools=form.langtools.data

        db.session.commit()
        flash('Project updated', 'success')
        return redirect(url_for('routes/main.projects'))
    
    elif request.method == 'GET':
        form.name.data=project.name
        form.description.data=project.description
        form.github.data=project.github
        form.link.data=project.link
        form.proj_type.data=project.type
        form.main_lang.data=project.main
        form.langtools.data=project.langtools

    return render_template('project_input.html', title='Update Project', form=form, user=current_user)