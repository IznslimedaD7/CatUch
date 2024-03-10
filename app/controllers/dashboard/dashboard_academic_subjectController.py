from flask import render_template, request, redirect, url_for
from app.blueprints.dashboard.academic_subject.form import AcademicSubjectForm
from app.repositories.academic_subjectRepository import AcademicSubjectRepository


class DashboardAcademicSubjectController():
    def index(page=1):
        academic_subjects = AcademicSubjectRepository.all_academic_subject_paginate(page, 10, False)
        return render_template('dashboard/academic_subject/index.html', academic_subjects=academic_subjects)
    
    def create():
        form = AcademicSubjectForm('/dashboard/academic_subjects/create')

        return render_template('dashboard/academic_subject/create.html.jinja', form=form)
    
    def store():
        title = request.form.get('title')

        AcademicSubjectRepository.store_academic_subject(title)

        return redirect(url_for('dashboard_academic_subject.index'))
    
    def edit(id):
        academic_subject = AcademicSubjectRepository.get_academic_subject_by_id(id)
        form = AcademicSubjectForm('/dashboard/academic_subjects/edit')
        return render_template('dashboard/academic_subject/edit.html.jinja', form=form, academic_subject=academic_subject)
    
    def update():
        id = request.form.get('id')
        title = request.form.get('title')

        AcademicSubjectRepository.update_academic_subject(id, title)

        return redirect(url_for('dashboard_academic_subject.index'))

