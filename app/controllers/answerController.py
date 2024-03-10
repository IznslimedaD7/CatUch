from flask import render_template, redirect, request, url_for
from app.blueprints.answer.form import AnswerForm
from app.repositories.questionRepository import QuestionRepository
from app.repositories.answerRepository import AnswerRepository
from flask_login import login_user, current_user, logout_user


class AnswerController():
    def create(id):
        form = AnswerForm('/answer/create')
        question = QuestionRepository.get_question_by_id(id)
        return render_template('answer/create.html.jinja', form=form, question=question)
    
    def store(id):
        body = request.form.get('body')
        question_id = QuestionRepository.get_question_by_id(id).id
        user_id = current_user.id

        AnswerRepository.create_answer(body, question_id, user_id)

        return redirect(url_for('question.view_question', id=id))


