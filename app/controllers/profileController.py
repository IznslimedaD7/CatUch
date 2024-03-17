from flask import render_template, redirect, request, url_for
from app.repositories.profileRepository import ProfileRepository
from app.repositories.questionRepository import QuestionRepository
from app.utils import format_data
from flask_login import login_user, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash


class ProfileController():
    def index(id):
        profile = ProfileRepository.get_profile(id)
        questions = QuestionRepository.user_question(profile.id)
        q_dates = format_data(QuestionRepository.user_question(profile.id))
        return render_template('profile/index.html.jinja', profile=profile, questions=questions, q_dates=q_dates)