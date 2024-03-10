from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length


class RegistrstionForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired(), Length(min=6, max=50)])
    nickname = StringField('Имя пользователя', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6, max=65)])
    
    