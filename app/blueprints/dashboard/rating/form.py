from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class RatingForm(FlaskForm):
    title = StringField('Название звания рейтинга', validators=[DataRequired()])
    description = StringField('описание звания рейтинга', validators=[DataRequired()])
