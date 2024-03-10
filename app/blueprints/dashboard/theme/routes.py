from app.blueprints.dashboard.theme import bp
from app.controllers.dashboard.dashboard_themeController import DashboardThemeController
from flask_login import login_required


@bp.get('/dashboard/theme/')
@bp.get('/dashboard/theme/<int:page>/')
def index(page=1):
    return DashboardThemeController.index(page)

@bp.get('/dashboard/theme/create/')
def create():
    return DashboardThemeController.create()

@bp.post('/dashboard/theme/store/')
def store():
    return DashboardThemeController.store()

@bp.get('/dashboard/theme/edit/<int:id>/')
def edit(id):
    return DashboardThemeController.edit(id)

@bp.post('/dashboard/theme/update/')
def update():
    return DashboardThemeController.update()