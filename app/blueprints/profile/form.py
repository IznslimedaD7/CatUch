from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    body = CKEditorField('Тело вопроса', validators=[DataRequired()])
    theme = SelectField('Тема', validators=[DataRequired()])