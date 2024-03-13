from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.storage import Storage


db = SQLAlchemy()
ma = Marshmallow()
store = Storage()