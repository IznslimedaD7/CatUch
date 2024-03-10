from app.extensions import db
from app.models.question import Question
from app.models.answer import Answer


class AnswerRepository():
    def create_answer(body, question_id, user_id):
        answer = Answer(body=body, question_id=question_id, user_id=user_id)
        
        try:
            db.session.add(answer)
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    def get_answer_to_question(id):
        return Answer.query.filter_by(question_id=id).all()