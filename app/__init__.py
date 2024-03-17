from flask import Flask
from config import Config
from flask_migrate import Migrate
from app.extensions import db
from app.extensions import login_manager
from app.extensions import ckeditor
from app.models.user import User



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    db.init_app(app)
    login_manager.init_app(app)
    Migrate(app, db)
    ckeditor.init_app(app)


    #Register Blueprints
    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.blueprints.dashboard.academic_subject import bp as dashboard_academic_subject_bp
    app.register_blueprint(dashboard_academic_subject_bp)

    from app.blueprints.dashboard.academic_class import bp as dashboard_academic_class_bp
    app.register_blueprint(dashboard_academic_class_bp)

    from app.blueprints.dashboard.theme import bp as dashboard_theme_bp
    app.register_blueprint(dashboard_theme_bp)

    from app.blueprints.dashboard.role import bp as dashboard_role_bp
    app.register_blueprint(dashboard_role_bp)

    from app.blueprints.dashboard.rating import bp as dashboard_rating_bp
    app.register_blueprint(dashboard_rating_bp)

    from app.blueprints.dashboard.question import bp as dashboard_question_bp
    app.register_blueprint(dashboard_question_bp)

    from app.blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.blueprints.question import bp as question_bp
    app.register_blueprint(question_bp)

    from app.blueprints.answer import bp as answer_bp
    app.register_blueprint(answer_bp)

    from app.blueprints.profile import bp as profile_bp
    app.register_blueprint(profile_bp)

    return app
    