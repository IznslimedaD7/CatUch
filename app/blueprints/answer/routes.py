from app.blueprints.answer import bp
from app.controllers.answerController import AnswerController
from flask_login import login_required


@bp.get('/question/<int:id>/create/')
def create(id):
    return AnswerController.create(id)

@bp.post('/question/<int:id>/store/')
def store(id):
    return AnswerController.store(id)

