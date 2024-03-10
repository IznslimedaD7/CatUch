from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class ThemeForm(FlaskForm):
    title = StringField('Название темы')
    academic_class = SelectField(
        'Выберите класс', validators=[DataRequired()])
    academic_subject = SelectField(
        'Выберите предмет', validators=[DataRequired()])