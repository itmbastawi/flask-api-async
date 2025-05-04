# app/__init__.py
from flask import Flask
from .extensions import db, migrate, ma, jwt
from .routes.auth import auth_bp
from .routes.api import api_bp
import os

def create_app(config=None):
    app = Flask(__name__)


    if config:
        app.config.from_object(config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(api_bp, url_prefix='/api')

    return app