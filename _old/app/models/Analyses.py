import datetime

class Analyses(db.Model):
    __tablename__ = 'analyses'
    id = db.Column(db.Integer, primary_key=True)    
    sysCreated = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    sysModified = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class AnalysesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "_links")

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("analysis", values=dict(id="<id>")),
            "collection": ma.URLFor("analysis"),
        }
    )
    

analysis_schema = AnalysesSchema()
analyses_schema = AnalysesSchema(many=True)   