from app.blueprints.dashboard.main import bp
from flask import render_template


@bp.route('/dashboard/')
def main():
    return render_template('dashboard/main/main.html')