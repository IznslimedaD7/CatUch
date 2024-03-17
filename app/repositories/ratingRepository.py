from app.extensions import db
from app.models.rating import Rating 
from app.models.question import Question
from app.models.answer import Answer

class RatingRepository():
    def all_rating_paginate(page, per_page, error_out):
        return Rating.query.paginate(page=page, per_page=per_page, error_out=error_out)
    
    def store_rating(title, description):
        rating = Rating(title=title, description=description)

        try:
            db.session.add(rating)
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    def get_rating_by_id(id):
        return Rating.query.filter_by(id=id).first()
    
    def update_rating(id, title, description):
        theme = RatingRepository.get_rating_by_id(id)
        theme.title = title
        theme.description = description

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()