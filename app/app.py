from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import os

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'uploads/'

class UploadForm(FlaskForm):
    file = FileField('XML File', validators=[DataRequired()])
    submit = SubmitField('Upload')

@app.route('/')
def home():
    form = UploadForm()
    return render_template('/home.html', form=form)

@app.route('/about')
def about():
    return render_template('/about.html')

@app.route('/upload', methods=['POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'success': True})
    return jsonify({'success': False})

@app.route('/version')
def version():
    return jsonify({'version': '1.0'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
