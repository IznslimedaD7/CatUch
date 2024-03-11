from app.extensions import db
from app.models.academic_class import Academic_class
from app.models.academic_subject import Academic_subject
from datetime import datetime


class Theme(db.Model):
    __tablename__ = 'themes'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    academic_class_id = db.Column(db.Integer, db.ForeignKey(Academic_class.id), nullable=False)
    academic_subject_id = db.Column(db.Integer, db.ForeignKey(Academic_subject.id), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    questions = db.relationship('Question', backref='theme')

    def __repr__(self):
        return '<Theme %r>' % self.id