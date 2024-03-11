from flask import render_template, request, redirect, url_for
from app.repositories.roleRepository import RoleRepository
from app.blueprints.dashboard.role.form import RoleForm


class DashboardRoleController():
    def index(page=1):
        roles = RoleRepository.all_role_paginate(page, 10, False)
        return render_template('dashboard/role/index.html', roles=roles)
    
    def create():
        form = RoleForm('/dashboard/role/create')

        return render_template('dashboard/role/create.html.jinja', form=form)
    
    def store():
        title = request.form.get('title')
        description = request.form.get('description')

        RoleRepository.store_role(title, description)

        return redirect(url_for('dashboard_role.index'))
    
    def edit(id):
        role = RoleRepository.get_role_by_id(id)
        form = RoleForm('/dashboard/role/edit')
        return render_template('dashboard/role/edit.html.jinja', form=form, role=role)
    
    def update():
        id = request.form.get('id')
        title = request.form.get('title')
        description = request.form.get('description')

        RoleRepository.update_role(id, title, description)

        return redirect(url_for('dashboard_role.index'))

