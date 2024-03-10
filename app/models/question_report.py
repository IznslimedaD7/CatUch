from app.extensions import db
from datetime import datetime
from app.models.question import Question


class Question_report(db.Model):
    __tablename__ = 'question_reports'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey(Question.id), nullable=False)
    
