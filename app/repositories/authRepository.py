from app.extensions import db
from app.models.user import User
from werkzeug.security import generate_password_hash
from app.models.question import Question
from app.models.answer import Answer


class AuthRepository():
    def register_user(login, nickname, email, password, avatar, score, rating_id, role_id):
        user = User(login=login, nickname=nickname, email=email, password=generate_password_hash(password),
                    avatar=avatar, score=score, rating_id=rating_id, role_id=role_id)
        
        try:
            db.session.add(user)
            db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            return 0

    def auth_user(login):
        return db.session.query(User).filter(
            User.login == login).first()
        