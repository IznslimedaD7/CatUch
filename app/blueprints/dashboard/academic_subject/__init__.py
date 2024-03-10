from flask import Blueprint

bp = Blueprint('dashboard_academic_subject', __name__)

from app.blueprints.dashboard.academic_subject import routes