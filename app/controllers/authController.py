from flask import render_template, redirect, request, url_for
from app.blueprints.auth.forms.registrationForm import RegistrstionForm
from app.blueprints.auth.forms.loginForm import LoginForm
from app.repositories.authRepository import AuthRepository
from flask_login import login_user, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash


class AuthController():
    def registeration():
        if current_user.is_authenticated:
            return redirect('/')

        form = RegistrstionForm('/registration/')
        return render_template('auth/register.html.jinja', form=form)
    
    def create():
        login = request.form.get("login")
        nickname = request.form.get("nickname")
        email = request.form.get("email")
        password = request.form.get("password")
        avatar = "default.jpg"
        score = 0
        rating_id = 1
        role_id = 1

        user = AuthRepository.register_user(login, nickname, email, password, avatar, score, rating_id, role_id)

        remember = True

        login_user(user, remember=remember)

        return redirect(url_for('main.main'))

    def login():
        if current_user.is_authenticated:
            return redirect('/')
        
        form = LoginForm('auth')
        return render_template('auth/login.html.jinja', form=form)

    def auth():
        user = AuthRepository.auth_user(request.form["login"])
        remember = True if request.form.get('remember') else False

        if user and check_password_hash(user.password, request.form['password']):
            login_user(user, remember=remember)
            return redirect('/')
        else:
            return redirect('/login')
        
    def logout():
        logout_user()
        return redirect('/')