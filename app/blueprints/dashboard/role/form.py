from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class RoleForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])