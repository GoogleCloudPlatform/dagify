import os
import uuid
import datetime
from flask import Flask, render_template, request, \
    jsonify, abort, Response, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from json import dumps


app = Flask(__name__, template_folder='dist', static_folder='dist')

app.config['PORT'] = int(os.environ.get('PORT', 5000))
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or str(uuid.uuid4())
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
app.config['UPLOAD_FOLDER'] = 'uploads/'

db = SQLAlchemy()
db.init_app(app)


# JSON Returns
def get_json(model):
    return {col.name: getattr(model, col.name) for col in model.__table__.columns}


def get_json_all(model):
    return jsonify([get_json(model) for c in model.query.all()])


class Conversions(db.Model):
    __tablename__ = 'conversions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    filename = db.Column(db.String(300))
    #sysCreated = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    #sysModified = db.Column(db.DateTime, default=datetime.datetime.utcnow)
        


#class ControlMFolders(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    folder_name = db.Column(db.String(80))
    # ... other folder details
    #conversion_id = db.Column(db.Integer, db.ForeignKey('conversions.id'))

    #control_m_jobs = db.relationship('ControlMJobs', backref='control_m_folder', lazy='dynamic')

#    def get_json(self):
#        return


#class ControlMJobs(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    job_name = db.Column(db.String(80))
    # ... other job details
    #control_m_folder_id = db.Column(db.Integer, db.ForeignKey('control_m_folders.id'))
    #control_m_operator_id = db.Column(db.Integer, db.ForeignKey('airflow_operators.id'))

    #control_m_operator = db.relationship('AirflowOperators', backref='control_m_job', uselist=False) 

 #   def get_json(self):
 #       return



@app.route('/api/v1/version')
def version():
    return jsonify({'version': 'v0.0.1'})


@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/test')
def test():
    return render_template('/test.html')


@app.route('/api/v1/conversions', methods=['GET', 'POST'])
@app.route('/api/v1/conversions/<int:conversion_id>', methods=['GET', 'POST', 'DELETE'])
def api_conversions(conversion_id=None):
    if request.method == 'POST':
        
        # Create New Conversion
        if conversion_id is None:
            # Handle POST request
            if 'file' not in request.files:
                print("MADE IT! error")
                error_message = 'No file part in the request'
                return Response(dumps({'Message': error_message}), 400)
        
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
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            
            print("MADE IT4")

            unique_filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '_' + str(uuid.uuid4())[0:5] + '_' + secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))

            # Create a new conversion
            conversion = Conversions(name=unique_filename, filename=unique_filename)
            db.session.add(conversion)
            db.session.commit()
            success_message = 'Conversion Project successfully Created'
            return Response(dumps({'conversion': get_json(conversion), 'status': 'Success', 'message': success_message}), 201)
        else: 
            # Update existing Conversion
            return 
    elif request.method == 'GET':
        if conversion_id is None:
            # Handle GET request for all conversions
            conversions = Conversions.query.all()
            return jsonify([c.get_json() for c in conversions])
        else:
            # Handle GET request for a specific conversion
            return
    elif request.method == 'DELETE':
        # Handle DELETE request
        return


@app.route('/api/v1/conversions/analyze/<int:conversion_id>', methods=['GET', 'POST', 'DELETE'])
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
        
            if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], conversion.filename)):
                error_message = 'Control-M xml file associated with conversion not found'
                return Response(dumps({'Message': error_message}), 400)
            
            # Analyze Conversion file
            success_message = 'Control-M xml file successfully analyzed'
            return Response(dumps({'status': 'Success', 'message': success_message}), 200)
    
    error_message = 'unable to analyze conversion'
    return Response(dumps({'Message': error_message}), 500)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['xml']


if __name__ == '__main__':   
    with app.app_context():  # Ensures db and session availability in routes
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=app.config['PORT'])
