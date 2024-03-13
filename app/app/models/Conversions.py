import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base
from app.extensions import db

Base = declarative_base()


class Conversions(Base):
    __tablename__ = 'conversions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=False)
    description = db.Column(db.String(500))
    filename = db.Column(db.String(300), nullable=False)
    sysCreated = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    sysModified = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    @validates("name")
    def validate_name(self, key, name):
        if len(name) <= 4:
            raise ValueError("conversions name must be at least 5 characters long")
        if len(name) > 200:
            raise ValueError("conversions name is too long must be less than 200 characters")
        return name

    @validates("description")
    def validate_description(self, key, description):
        if len(description) > 500:
            raise ValueError("conversions description is too long must be less than 500 characters")
        return description


class ConversionsSchema(SQLAlchemyAutoSchema):
   class Meta:
        model = Conversions
        include_relationships = True
        load_instance = True


conversion_schema = ConversionsSchema()
conversions_schema = ConversionsSchema(many=True)    
