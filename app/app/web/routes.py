from flask import render_template, jsonify
from app.core import bp

@bp.route('/')
def home():
    return render_template('/index.html')