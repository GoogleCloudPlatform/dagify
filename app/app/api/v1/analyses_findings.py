from flask import request, jsonify
from app.api.v1 import bp


@bp.route('/findings', methods=['GET', 'POST'])
def api_findings(conversion_id=None):
    if request.method == 'GET':
        return jsonify({'endpoint': 'findings'})