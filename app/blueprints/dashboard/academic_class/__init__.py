from flask import Blueprint

bp = Blueprint('dashboard_academic_class', __name__)

from app.blueprints.dashboard.academic_class import routes