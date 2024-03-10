from app.blueprints.dashboard.academic_class import bp
from flask import render_template
from app.controllers.dashboard.dashboard_academic_classController import DashboardAcademicClassController
from flask_login import login_required


@bp.get('/dashboard/academic_classes/')
@bp.get('/dashboard/academic_classes/<int:page>/')
@login_required
def index(page=1):
    return DashboardAcademicClassController.index(page)

@bp.get('/dashboard/academic_classes/create/')
def create():
    return DashboardAcademicClassController.create()

@bp.post('/dashboard/academic_classes/store/')
def store():
    return DashboardAcademicClassController.store()

@bp.get('/dashboard/academic_classes/edit/<int:id>/')
def edit(id):
    return DashboardAcademicClassController.edit(id)

@bp.post('/dashboard/academic_classes/update/')
def update():
    return DashboardAcademicClassController.update()