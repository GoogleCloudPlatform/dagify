from flask import render_template
from app.core import bp


@bp.route('/')
def home():
    print("hitting...")
    return render_template('/index.html')
