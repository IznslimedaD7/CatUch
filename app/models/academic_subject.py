from app.extensions import db
from datetime import datetime


class Academic_subject(db.Model):
    __tablename__ = 'academic_subjects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)

    themes = db.relationship('Theme', backref='academic_subject')

    def __repr__(self):
        return '<Academic Subjects %r>' % self.id