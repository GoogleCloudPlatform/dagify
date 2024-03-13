import os
import uuid
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


##########################################
############## APP SETUP #################
##########################################
app = Flask(__name__, template_folder='dist', static_folder='dist')
app.config['PORT'] = int(os.environ.get('PORT', 5000))
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or str(uuid.uuid4())
app.config['UPLOAD_FOLDER'] = 'files/uploads/'
app.config['DOWNLOADS_FOLDER'] = 'files/outputs/'
app.config['CONVERSION_TEMPLATES_FOLDER'] = 'files/templates/'


##########################################
############ DATABASE SETUP ##############
##########################################
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'airflow_agent.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)
ma = Marshmallow(app)


##########################################
######### REGISTER BLUEPRINTS ############
##########################################
from project.routes import conversions

app.register_blueprint(core.bp, url_prefix='/api/v1')
app.register_blueprint(conversions.bp, url_prefix='/api/v1')
app.register_blueprint(analyses.bp, url_prefix='/api/v1')
app.register_blueprint(findings.bp, url_prefix='/api/v1')



