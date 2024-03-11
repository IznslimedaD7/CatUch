from flask import render_template, redirect, request, url_for
from app.blueprints.question.form import QuestionForm
from app.repositories.themeRepository import ThemeRepository
from app.repositories.questionRepository import QuestionRepository
from app.repositories.answerRepository import AnswerRepository
from flask_login import login_user, current_user, logout_user


class QuestionController():
    def create():
        form = QuestionForm('/question/create')
        form.theme.choices = [(s.id, f'{s.academic_subject.title} {s.academic_class.title}, {s.title}')
                              for s in ThemeRepository.theme_choices()]
        return render_template('question/create.html.jinja', form=form)
    
    def store():
        title = request.form.get('title')
        body = request.form.get('body')
        likes = 0
        user_id = current_user.id
        themes_id = request.form.get('theme')

        question = QuestionRepository.store_question(title, body, likes, user_id, themes_id)

        return redirect(f'/question/{question.id}')

    def view_question(id):
        question = QuestionRepository.get_question_by_id(id)
        answers = AnswerRepository.get_answer_to_question(id)
        return render_template('question/view.html.jinja', question=question, answers=answers)
