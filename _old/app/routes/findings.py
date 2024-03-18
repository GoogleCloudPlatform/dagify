from json import dumps
from flask import current_app, request, Response, Blueprint
from models import AnalysisFindings

bp = Blueprint('findings', __name__)


@bp.route('/conversions/<int:conversion_id>/analysis/<int:analysis_id>/findings', methods=['GET'])
@bp.route('/conversions/<int:conversion_id>/analysis/<int:analysis_id>/findings/<int:finding_id>', methods=['GET'])
def analysis_findings(conversion_id, analysis_id, finding_id):
    if request.method == 'GET':
        # Analyze Existing Finding
        if finding_id is None:
            error_message = 'No analysis finding ID provided'
            return Response(dumps({'Message': error_message}), 400)

        # Analyze existing Conversion
        finding = AnalysisFindings.query.filter_by(id=finding_id).first()
        if finding is None:
            error_message = 'Analysis finding ID not found'
            return Response(dumps({'Message': error_message}), 400)