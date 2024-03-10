from app.extensions import db
from app.models.user import User


class ProfileRepository():
    def get_profile(id):
        return User.query.filter_by(id=id).first()