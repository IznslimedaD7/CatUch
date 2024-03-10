from app.extensions import db
from datetime import datetime
from app.models.user import User
from app.models.theme import Theme


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    themes_id = db.Column(db.Integer, db.ForeignKey(Theme.id), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    answers = db.relationship('Answer', backref='question')
    reports = db.relationship('Question_report', backref='question')
    