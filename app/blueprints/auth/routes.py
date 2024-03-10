from app.blueprints.auth import bp
from app.controllers.authController import AuthController


@bp.get('/registration/')
def registration():
    return AuthController.registeration()

@bp.post('/auth/create/')
def create():
    return AuthController.create()

@bp.get('/login/')
def login():
    return AuthController.login()

@bp.post('/auth/auth/')
def auth():
    return AuthController.auth()

@bp.route('/logout/')
def logout():
    return AuthController.logout()
