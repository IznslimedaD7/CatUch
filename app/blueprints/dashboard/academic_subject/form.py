from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class AcademicSubjectForm(FlaskForm):
    title = StringField('Название предмета', validators=[DataRequired()])
