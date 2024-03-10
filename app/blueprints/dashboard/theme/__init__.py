from flask import Blueprint

bp = Blueprint('dashboard_theme', __name__)

from app.blueprints.dashboard.theme import routes