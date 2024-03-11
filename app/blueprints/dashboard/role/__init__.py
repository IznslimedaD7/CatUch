from flask import Blueprint

bp = Blueprint('dashboard_role', __name__)

from app.blueprints.dashboard.role import routes