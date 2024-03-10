from app.extensions import db
from datetime import datetime


class Academic_class(db.Model):
    __tablename__ = 'academic_classes'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)

    themes = db.relationship('Theme', backref='academic_class')

    def __repr__(self):
        return '<Academic Class %r>' % self.id