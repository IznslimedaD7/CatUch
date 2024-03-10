from app.extensions import db
from datetime import datetime
from app.models.answer import Answer


class Answer_report(db.Model):
    __tablename__ = 'answer_reports'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    answer_id = db.Column(db.Integer, db.ForeignKey(Answer.id), nullable=False)