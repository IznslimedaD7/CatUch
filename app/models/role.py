from app.extensions import db
from datetime import datetime


class Role(db.Model):
    __tablename__ = 'roles'

    _role_admin = 1
    _role_user = 2

    @property
    def role_admin(self):
        return type(self)._role_admin
    
    @property
    def role_user(self):
        return type(self)._role_user
    

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text())
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.id