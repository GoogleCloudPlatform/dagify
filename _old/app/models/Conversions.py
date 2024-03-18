import datetime
from flask import current_app


with current_app.app_context(): 
    class Conversions(current_app.db.Model):
        __tablename__ = 'conversions'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), unique=True)
        filename = db.Column(db.String(300))
        sysCreated = db.Column(db.DateTime, default=datetime.datetime.utcnow)
        sysModified = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    class ConversionsSchema(ma.Schema):
        class Meta:
            # Fields to expose
            fields = ("id", "name", "filename", "sysCreated", "sysModified", "_links")

        # Smart hyperlinking
        _links = ma.Hyperlinks(
            {
                "self": ma.URLFor("api_conversions", values=dict(id="<id>")),
                "collection": ma.URLFor("api_conversions"),
            }
        )

    conversion_schema = ConversionsSchema()
    conversions_schema = ConversionsSchema(many=True)    
