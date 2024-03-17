from flask import render_template, request, redirect, url_for
from app.repositories.questionRepository import QuestionRepository


class DashboardQuetionController():
    def index():
        questions = QuestionRepository.all_question()
        return render_template('dashboard/question/index.html.jinja', questions=questions)