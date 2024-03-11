from app.blueprints.dashboard.academic_subject import bp
from flask import render_template
from app.controllers.dashboard.dashboard_academic_subjectController import DashboardAcademicSubjectController
from flask_login import login_required


@bp.get('/dashboard/academic_subjects/')
@bp.get('/dashboard/academic_subjects/<int:page>/')
def index(page=1):
    return DashboardAcademicSubjectController.index(page)

@bp.get('/dashboard/academic_subjects/create/')
def create():
    return DashboardAcademicSubjectController.create()

@bp.post('/dashboard/academic_subjects/store/')
def store():
    return DashboardAcademicSubjectController.store()

@bp.get('/dashboard/academic_subjects/edit/<int:id>/')
def edit(id):
    return DashboardAcademicSubjectController.edit(id)

@bp.post('/dashboard/academic_subjects/update/')
def update():
    return DashboardAcademicSubjectController.update()