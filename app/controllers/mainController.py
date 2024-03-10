from app.repositories.academic_subjectRepository import AcademicSubjectRepository
from app.repositories.questionRepository import QuestionRepository
from flask import render_template


class MainController():
    def main():
        subjects = AcademicSubjectRepository.academic_subject_choices()
        questions = QuestionRepository.all_question()
        return render_template('main/main.html', subjects=subjects, questions=questions)
