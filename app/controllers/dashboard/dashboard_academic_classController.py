from flask import render_template, request, redirect, url_for
from app.blueprints.dashboard.academic_class.form import AcademicClassForm
from app.repositories.academic_classRepository import AcademicClassRepository


class DashboardAcademicClassController():
    def index(page=1):
        academic_classes = AcademicClassRepository.all_academic_class_paginate(page, 10, False)
        return render_template('dashboard/academic_class/index.html.jinja', academic_classes=academic_classes)
    
    def create():
        form = AcademicClassForm('/dashboard/academic_class/create')

        return render_template('dashboard/academic_class/create.html.jinja', form=form)
    
    def store():
        title = request.form.get('title')

        AcademicClassRepository.store_academic_class(title)

        return redirect(url_for('dashboard_academic_class.index'))
    
    def edit(id):
        academic_class = AcademicClassRepository.get_academic_class_by_id(id)
        form = AcademicClassForm('/dashboard/academic_class/edit')
        return render_template('dashboard/academic_class/edit.html.jinja', form=form, academic_class=academic_class)
    
    def update():
        id = request.form.get('id')
        title = request.form.get('title')

        AcademicClassRepository.update_academic_class(id, title)

        return redirect(url_for('dashboard_academic_class.index'))