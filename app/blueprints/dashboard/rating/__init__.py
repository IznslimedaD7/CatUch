from flask import Blueprint

bp = Blueprint('dashboard_rating', __name__)

from app.blueprints.dashboard.rating import routes
