from flask import Blueprint

bp = Blueprint('question', __name__)

from app.blueprints.question import routes