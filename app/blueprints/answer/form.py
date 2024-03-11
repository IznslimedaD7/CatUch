from flask_wtf import FlaskForm
from wtforms import StringField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired


class AnswerForm(FlaskForm):
    body = CKEditorField('Ответ', validators=[DataRequired()])