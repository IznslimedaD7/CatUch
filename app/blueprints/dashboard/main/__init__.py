from flask import Blueprint

bp = Blueprint('dashboard_main', __name__)

from app.blueprints.dashboard.main import routes