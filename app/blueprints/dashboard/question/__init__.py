from flask import Blueprint

bp = Blueprint('dashboard_question', __name__)

from app.blueprints.dashboard.question import routes