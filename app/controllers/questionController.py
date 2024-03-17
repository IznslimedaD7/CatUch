from flask import render_template, redirect, request, url_for
from app.blueprints.question.form import QuestionForm
from app.repositories.themeRepository import ThemeRepository
from app.repositories.academic_subjectRepository import AcademicSubjectRepository
from app.repositories.questionRepository import QuestionRepository
from app.repositories.answerRepository import AnswerRepository
from app.utils import format_data
from flask_login import login_user, current_user, logout_user


class QuestionController():
    def index(id):
        if id == 0:
            sub = "Все"
            questions = QuestionRepository.all_question()
        else:
            sub = AcademicSubjectRepository.get_academic_subject_by_id(id).title
            questions = QuestionRepository.quetion_by_theme(AcademicSubjectRepository.get_academic_subject_by_id(id).id)
        subjects = AcademicSubjectRepository.academic_subject_choices()
        q_dates = format_data(questions)

        return render_template('question/index.html.jinja', sub=sub, subjects=subjects, questions=questions, q_dates=q_dates)
    
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
        q_dates = format_data([question])[0]

        return render_template('question/view.html.jinja', question=question, answers=answers, q_dates=q_dates)
