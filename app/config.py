import os
import uuid

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Flask Secret Key
    SECRET_KEY = os.environ.get('SECRET_KEY') or str(uuid.uuid4())
    # Flask Static Assets Folder
    STATIC_FOLDER = os.environ.get('STATIC_FOLDER') \
        or "web/dist/"
    # Flask Template Folder
    TEMPLATE_FOLDER = os.environ.get('TEMPLATE_FOLDER') \
        or "web/dist/"
    # SQLAlchemy Database Connection String
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLAlchemy Track Modifications Flag
    SQLALCHEMY_TRACK_MODIFICATIONS = \
        os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') \
        or False
    # Upload Folder Path & Name
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') \
        or 'files/uploads/'
    # Output Folder Path & Name
    DOWNLOADS_FOLDER = os.environ.get('DOWNLOADS_FOLDER') \
        or 'files/outputs/'
    # Templates Folder Path & Name
    HTML_TEMPLATES_FOLDER = os.environ.get('HTML_TEMPLATES_FOLDER') \
        or 'files/templates/'
    # Flask Debug Mode Flag
    DEBUG = os.environ.get('DEBUG') \
        or False
    # Flask Testing Mode Flag
    TESTING = os.environ.get('TESTING') \
        or False
    # Maintenance GitHub Repo
    MAINTENANCE_GITHUB_REPO_URL = \
        os.environ.get('MAINTENANCE_GITHUB_REPO_URL') \
        or "https://github.com/KonradSchieban/cntrlm-to-airflow/issues"