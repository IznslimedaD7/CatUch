from app.blueprints.dashboard.question import bp
from flask import render_template
from app.controllers.dashboard.dashboard_questionController import DashboardQuetionController
from flask_login import login_required


@bp.get('/dashboard/questions/')
def index():
    return DashboardQuetionController.index()

