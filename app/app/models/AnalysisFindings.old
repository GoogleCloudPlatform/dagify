import datetime

class AnalysisFindings(db.Model):
    __tablename__ = 'analysis_findings'
    id = db.Column(db.Integer, primary_key=True)    
    sysCreated = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    sysModified = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class AnalysisFindingsSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "_links")

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("analysis_findings", values=dict(id="<id>")),
            "collection": ma.URLFor("analysis_findings"),
        }
    )


analysis_findings_schema = AnalysisFindings()
analysis_findings_schema = AnalysisFindingsSchema(many=True)    