from flask import render_template, redirect, request, url_for
from app.repositories.profileRepository import ProfileRepository
from flask_login import login_user, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash


class ProfileController():
    def index(id):
        profile = ProfileRepository.get_profile(id)
        return render_template('profile/index.html.jinja', profile=profile)