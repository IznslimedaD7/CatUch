from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class AcademicClassForm(FlaskForm):
    title = StringField('Название класса', validators=[DataRequired()])
