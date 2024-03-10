from app.extensions import db
from app.extensions import login_manager
from flask_login import UserMixin
from datetime import datetime
from app.models.role import Role
from app.models.rating import Rating


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), nullable=False, unique=True)
    nickname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    avatar = db.Column(db.String(100))
    score = db.Column(db.Integer)
    rating_id = db.Column(db.Integer, db.ForeignKey(Rating.id), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    questions = db.relationship('Question', backref='user')
    answers = db.relationship('Answer', backref='user')
    
    def isAdmin(self):
        return True if self.role_id == Role._role_admin else False
    
    def __repr__(self):
        return '<User %r>' % self.id
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))