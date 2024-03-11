from app.blueprints.main import bp
from flask import render_template
from app.controllers.mainController import MainController


@bp.route('/')
def main():
    return MainController.main()