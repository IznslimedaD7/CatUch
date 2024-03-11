from app.extensions import db
from app.models.academic_class import Academic_class

class AcademicClassRepository():
    def all_academic_class_paginate(page, per_page, error_out):
        return Academic_class.query.paginate(page=page, per_page=per_page, error_out=error_out)

    def store_academic_class(title):
        academic_class = Academic_class(title=title)

        try:
            db.session.add(academic_class)
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    def get_academic_class_by_id(id):
        return Academic_class.query.filter_by(id=id).first()
    
    def update_academic_class(id, title):
        academic_class = AcademicClassRepository.get_academic_class_by_id(id)
        
        academic_class.title = title

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    def academic_class_choices():
        return Academic_class.query.all()