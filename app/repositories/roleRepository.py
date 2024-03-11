from app.extensions import db
from app.models.role import Role
from app.models.question import Question
from app.models.answer import Answer

class RoleRepository():
    def all_role_paginate(page, per_page, error_out):
        return Role.query.paginate(page=page, per_page=per_page, error_out=error_out)

    def store_role(title, description):
        role = Role(title=title, description=description)

        try:
            db.session.add(role)
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    def get_role_by_id(id):
        return Role.query.filter_by(id=id).first()
    
    def update_role(id, title, description):
        theme = RoleRepository.get_role_by_id(id)
        theme.title = title
        theme.description = description

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()