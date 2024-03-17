from app.repositories.academic_subjectRepository import AcademicSubjectRepository
from app.repositories.questionRepository import QuestionRepository
from app.utils import format_data
from flask import render_template


class MainController():
    def main():
        subjects = AcademicSubjectRepository.academic_subject_choices()
        questions = QuestionRepository.all_question()[-3:]
        q_dates = format_data(QuestionRepository.all_question()[-3:])
        return render_template('main/main.html.jinja', subjects=subjects, questions=questions, q_dates=q_dates)
