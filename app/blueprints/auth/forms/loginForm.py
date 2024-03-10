from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Length, DataRequired


class LoginForm(FlaskForm):
    login = StringField('Имя пользователя', validators=[DataRequired(), Length(
        min=5, max=50)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField("Запомнить", default=False)