import os
import uuid
import datetime
from flask import Flask, render_template, request, \
    jsonify, abort, Response, flash
from werkzeug.utils import secure_filename
from json import dumps


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or str(uuid.uuid4())
app.config['UPLOAD_FOLDER'] = 'uploads/'


@app.route('/api/v1/version')
def version():
    return jsonify({'version': '1.0'})


@app.route('/')
def home():
    return render_template('/index.html')


@app.route('/about')
def about():
    return render_template('/about.html')


@app.route('/faq')
def faq():
    return render_template('/faq.html')


@app.route('/convert')
def convert():
    return render_template('/convert.html')


@app.route('/api/v1/convert/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        error_message = 'No file part in the request'
        flash(error_message, 'danger')
        abort(Response(dumps({'Message': error_message}), 400))

    file = request.files['file']

    if file.filename == '':
        error_message = 'No file selected for uploading'
        flash(error_message, 'danger')
        abort(Response(dumps({'Message': error_message}), 400))

    if not allowed_file(file.filename):
        error_message = 'File type not allowed'
        flash(error_message, 'danger')
        abort(Response(dumps({'Message': error_message}), 400))      

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    unique_filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '_' + str(uuid.uuid4())[0:5] + '_' + secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))

    flash("File successfully uploaded", 'success')
    return jsonify({'success': True, 'filename': unique_filename})


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['xml']


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
