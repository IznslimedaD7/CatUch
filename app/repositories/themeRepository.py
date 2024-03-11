from app.extensions import db
from app.models.theme import Theme
from app.models.question import Question
from app.models.question_report import Question_report
from app.models.answer import Answer
from app.models.answer_report import Answer_report

class ThemeRepository():
    def all_theme_paginate(page, per_page, error_out):
        return Theme.query.paginate(page=page, per_page=per_page, error_out=error_out)

    def store_theme(title, academic_class, academic_subject):
        theme = Theme(title=title, academic_class_id=academic_class, academic_subject_id=academic_subject)

        try:
            db.session.add(theme)
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    def get_theme_by_id(id):
        return Theme.query.filter_by(id=id).first()
    
    def update_theme(id, title, academic_class, academic_subject):
        theme = ThemeRepository.get_theme_by_id(id)
        theme.title = title
        theme.academic_class_id = academic_class
        theme.academic_subject_id = academic_subject

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    def theme_choices():
        return Theme.query.all()