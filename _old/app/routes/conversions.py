import os
import uuid
import datetime
from json import dumps
from werkzeug.utils import secure_filename
from flask import current_app, request, Response, Blueprint
from models import Conversions, conversion_schema, conversions_schema

bp = Blueprint('conversions', __name__)


@bp.route('/conversions', methods=['GET', 'POST'])
@bp.route('/conversions/<int:conversion_id>', methods=['GET', 'POST', 'DELETE'])
def api_conversions(conversion_id=None):
    if request.method == 'POST':
        # Create New Conversion
        if conversion_id is None:
            # Handle POST request
            if 'file' not in request.files:
                error_message = 'No file part in the request'
                return Response(dumps({'message': error_message}), 400)

            # Get the file from the request
            file = request.files['file']

            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                error_message = 'No file selected for uploading'
                return Response(dumps({'message': error_message}), 400)

            # Check if the file extension is allowed
            if not allowed_file(file.filename):
                error_message = 'File type not allowed'
                return Response(dumps({'message': error_message}), 400)

            # Create uploads folder if it does not exist
            if not os.path.exists(current_app.config['UPLOAD_FOLDER']):
                os.makedirs(current_app.config['UPLOAD_FOLDER'])

            # Generate unique filename
            unique_filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '_' + str(uuid.uuid4())[0:5] + '_' + secure_filename(file.filename)

            # Save the file
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename))

            # Create a new conversion
            conversion = Conversions(name=unique_filename, filename=unique_filename)
            current_app.db.session.add(conversion)
            current_app.db.session.commit()
            success_message = 'Conversion Project successfully Created'
            return Response(dumps({
                'conversion':conversion_schema.dump(conversion),
                'status': 'Success',
                'message': success_message
            }), 201)
        else:
            # Update existing Conversion
            return
    elif request.method == 'GET':
        if conversion_id is None:
            # Handle GET request for all conversions
            conversions = Conversions.query.all()
            print(conversions)
            return conversions_schema.dump(conversions)
        else:
            # Handle GET request for a specific conversion
            return
    elif request.method == 'DELETE':
        # Handle DELETE request
        return
      
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['xml']