import logging
import uuid
from flask import request, jsonify, session
from app.api.v1 import bp

log = logging.getLogger(__name__)


@bp.route('/healthz', methods=['GET'])
def api_healthz():
    if request.method == 'GET':
        return jsonify({'healthz': True})


@bp.route('/version', methods=['GET'])
def api_version():
    if request.method == 'GET':
        return jsonify({'version': 'v0.0.1'})


@bp.route('/app', methods=['GET'])
def api_app():
    if request.method == 'GET':
        return jsonify({'appName': 'AirShip'})


@bp.before_request
def logBeforeRequest():
    session["ctx"] = {"request_id": str(uuid.uuid4())}


@bp.after_request
def logAfterRequest(response):
    log.info(
        "path: %s | method: %s | status: %s | size: %s >>> %s",
        request.path,
        request.method,
        response.status,
        response.content_length,
        session["ctx"],
    )

    return response
