from app.blueprints.dashboard.role import bp
from app.controllers.dashboard.dashboard_roleController import DashboardRoleController


@bp.get('/dashboard/role/')
@bp.get('/dashboard/role/<int:page>/')
def index(page=1):
    return DashboardRoleController.index(page)

@bp.get('/dashboard/role/create/')
def create():
    return DashboardRoleController.create()

@bp.post('/dashboard/role/store/')
def store():
    return DashboardRoleController.store()

@bp.get('/dashboard/role/edit/<int:id>/')
def edit(id):
    return DashboardRoleController.edit(id)

@bp.post('/dashboard/role/update/')
def update():
    return DashboardRoleController.update()
