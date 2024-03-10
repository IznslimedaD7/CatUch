from app.extensions import db
from app.models.question import Question
from app.models.answer import Answer


class QuestionRepository():
    def store_question(title, body, likes, user_id, themes_id):
        question = Question(title=title, body=body, likes=likes, user_id=user_id, themes_id=themes_id)
        
        try:
            db.session.add(question)
            db.session.commit()
            return question
        except Exception as e:
            db.session.rollback()
            return 0

    def get_question_by_id(id):
        return Question.query.filter_by(id=id).first()
    
    def all_question():
        return Question.query.all()