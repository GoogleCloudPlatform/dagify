import os
from json import dumps
from flask import current_app, request, Response, Blueprint
from .models import Conversions

bp = Blueprint('analyses', __name__)


@bp.route('/conversions/<int:conversion_id>/analyze', methods=['POST'])
def analyze(conversion_id):
    if request.method == 'POST':
        # Analyze Existing Conversion
        if conversion_id is None:
            error_message = 'No conversion ID provided'
            return Response(dumps({'Message': error_message}), 400)

        # Analyze existing Conversion
        # Find Conversion in Database
        conversion = Conversions.query.filter_by(id=conversion_id).first()
        if conversion is None:
            error_message = 'Conversion ID not found'
            return Response(dumps({'Message': error_message}), 400)
        else:
            # Find Conversion file
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                error_message = 'Control-M xml file associated with conversion not found'
                return Response(dumps({'Message': error_message}), 400)

            if not os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], conversion.filename)):
                error_message = 'Control-M xml file associated with conversion not found'
                return Response(dumps({'Message': error_message}), 400)


            # Analyze Conversion file
            cmp = parser.ControlMParser(xml_path=os.path.join(current_app.config['UPLOAD_FOLDER'], conversion.filename))
            cmp.analyze()
            success_message = 'Control-M xml file successfully analyzed'
            return Response(dumps({'status': 'Success', 'message': success_message}), 200)

    error_message = 'unable to analyze conversion'
    return Response(dumps({'Message': error_message}), 500)