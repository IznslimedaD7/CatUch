from flask import Blueprint

bp = Blueprint('answer', __name__)

from app.blueprints.answer import routes