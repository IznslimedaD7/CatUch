from app.blueprints.question import bp
from app.controllers.questionController import QuestionController
from flask_login import login_required


@bp.get('/questions/')
@bp.get('/questions/<id>')
def index(id=0):
    return QuestionController.index(id)

@bp.get('/question/create/')
def create():
    return QuestionController.create()

@bp.post('/question/store/')
def store():
    return QuestionController.store()

@bp.get('/question/<int:id>')
def view_question(id):
    return QuestionController.view_question(id)