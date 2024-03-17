from app.blueprints.dashboard.rating import bp
from flask import render_template
from app.controllers.dashboard.dashboard_ratingController import DashboardRatingController


@bp.get('/dashboard/rating/')
@bp.get('/dashboard/rating/<int:page>/')
def index(page=1):
    return DashboardRatingController.index(page)

@bp.get('/dashboard/rating/create/')
def create():
    return DashboardRatingController.create()

@bp.post('/dashboard/rating/store/')
def store():
    return DashboardRatingController.store()

@bp.get('/dashboard/rating/edit/<int:id>/')
def edit(id):
    return DashboardRatingController.edit(id)

@bp.post('/dashboard/rating/update/')
def update():
    return DashboardRatingController.update()