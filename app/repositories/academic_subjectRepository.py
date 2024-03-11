from app.extensions import db
from app.models.academic_subject import Academic_subject
from app.models.question import Question
from app.models.answer import Answer

class AcademicSubjectRepository():
    def all_academic_subject_paginate(page, per_page, error_out):
        return Academic_subject.query.paginate(page=page, per_page=per_page, error_out=error_out)

    def store_academic_subject(title):
        academic_subject = Academic_subject(title=title)

        try:
            db.session.add(academic_subject)
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    def get_academic_subject_by_id(id):
        return Academic_subject.query.filter_by(id=id).first()
    
    def update_academic_subject(id, title):
        academic_subject = AcademicSubjectRepository.get_academic_subject_by_id(id)
        
        academic_subject.title = title

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    def academic_subject_choices():
        return Academic_subject.query.all()
    