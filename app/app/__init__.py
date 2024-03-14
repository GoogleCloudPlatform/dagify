import logging
import os
import sys
from flask import Flask, render_template
from logging.config import dictConfig
from config import Config
from app.extensions import db, ma, store


log = logging.getLogger(__name__)

# Add Converter to PATH
# TODO confirm this approach
sys.path.insert(0, os.getcwd() + "/converters")


def create_app(config_class=Config):
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] [%(levelname)s | %(module)s] %(message)s",
                    "datefmt": "%B %d, %Y %H:%M:%S %Z",
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                },
                "file": {
                    "class": "logging.FileHandler",
                    "filename": "logfile.log",
                    "formatter": "default",
                },
            },
            "root": {
                "level": "DEBUG",
                "handlers": [
                    "console",
                    "file"]},
        })

    app = Flask(__name__)
    app.config.from_object(config_class)
    # app.static_folder = app.config["STATIC_FOLDER"]
    # app.template_folder = app.config["TEMPLATE_FOLDER"]

    # Initialize Flask extensions
    try:
        db.init_app(app)        # SQLAlchemy
        ma.init_app(app)        # Marshmallow
        store.init_app(app)     # Storage
    except Exception as e:
        log.error("exiting, failed to initialize flask extensions", e)
        raise SystemExit

    # Import Database Models
    from app.models.Conversions import Conversions

    # Configure Database
    with app.app_context():
        db.create_all()

    # Register blueprints here
    from app.web import bp as web_bp
    app.register_blueprint(web_bp)

    from app.core import bp as core_bp
    app.register_blueprint(core_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app
