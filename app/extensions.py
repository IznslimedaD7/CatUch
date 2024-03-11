from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_ckeditor import CKEditor


db = SQLAlchemy()

login_manager = LoginManager()

ckeditor = CKEditor()
