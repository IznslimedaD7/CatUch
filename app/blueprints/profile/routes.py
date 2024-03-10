from app.blueprints.profile import bp
from app.controllers.profileController import  ProfileController
from flask_login import login_required


@bp.get("/profile/<int:id>/")
def index(id):
    return ProfileController.index(id)

