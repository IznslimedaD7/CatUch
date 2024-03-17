from flask import render_template, request, redirect, url_for
from app.blueprints.dashboard.theme.form import ThemeForm
from app.repositories.themeRepository import ThemeRepository
from app.repositories.academic_classRepository import AcademicClassRepository
from app.repositories.academic_subjectRepository import AcademicSubjectRepository


class DashboardThemeController():
    def index(page=1):
        themes = ThemeRepository.all_theme_paginate(page, 10, False)
        return render_template('dashboard/theme/index.html.jinja', themes=themes)
    
    def create():
        form = ThemeForm('/dashboard/theme/create')
        form.academic_class.choices = [(s.id, s.title)
                                for s in AcademicClassRepository.academic_class_choices()]
        form.academic_subject.choices = [(s.id, s.title)
                                for s in AcademicSubjectRepository.academic_subject_choices()]

        return render_template('dashboard/theme/create.html.jinja', form=form)
    
    def store():
        title = request.form.get('title')
        academic_class = request.form.get('academic_class')
        academic_subject = request.form.get('academic_subject')

        ThemeRepository.store_theme(title, academic_class, academic_subject)

        return redirect(url_for('dashboard_theme.index'))
    
    def edit(id):
        theme = ThemeRepository.get_theme_by_id(id)
        form = ThemeForm('/dashboard/theme/edit')
        form.academic_class.choices = [(s.id, s.title)
                                for s in AcademicClassRepository.academic_class_choices()]
        form.academic_class.process_data(theme.academic_class.id)
        form.academic_subject.choices = [(s.id, s.title)
                                for s in AcademicSubjectRepository.academic_subject_choices()]
        form.academic_subject.process_data(theme.academic_subject.id)
        return render_template('dashboard/theme/edit.html.jinja', form=form, theme=theme)
    
    def update():
        id = request.form.get('id')
        title = request.form.get('title')
        academic_class = request.form.get('academic_class')
        academic_subject = request.form.get('academic_subject')

        ThemeRepository.update_theme(id, title, academic_class, academic_subject)

        return redirect(url_for('dashboard_theme.index'))

