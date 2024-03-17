from flask import render_template, request, redirect, url_for
from app.blueprints.dashboard.rating.form import RatingForm
from app.repositories.ratingRepository import RatingRepository


class DashboardRatingController():
    def index(page=1):
        ratings = RatingRepository.all_rating_paginate(page, 10, False)
        return render_template('dashboard/rating/index.html.jinja', ratings=ratings)
    
    def create():
        form = RatingForm('/dashboard/rating/create')

        return render_template('dashboard/rating/create.html.jinja', form=form)
    
    def store():
        title = request.form.get('title')
        description = request.form.get('description')

        RatingRepository.store_rating(title, description)

        return redirect(url_for('dashboard_rating.index'))
    
    def edit(id):
        rating = RatingRepository.get_rating_by_id(id)
        form = RatingForm('/dashboard/rating/edit')
        return render_template('dashboard/rating/edit.html.jinja', form=form, rating=rating)
    
    def update():
        id = request.form.get('id')
        title = request.form.get('title')
        description = request.form.get('description')

        RatingRepository.update_rating(id, title, description)

        return redirect(url_for('dashboard_rating.index'))

