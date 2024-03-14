from flask import Response
from marshmallow import Schema, fields
from json import dumps


def HandleResponse(code=None, message=None,
                   payload=None, errors=None, status=None):
    """
    This function handles the response for API endpoints.

    Args:
        code (int): The HTTP status code to return.
        message (str): The message to return.

    Returns:
        Response: A Flask Response object.
    """

    # Construct Response
    output = {}
    output['message'] = message
    output['status'] = status
    output['errors'] = []
    output['payload'] = {}

    match code:
        case 200:
            if output['message'] is None:
                output['message'] = "Success"
            if output['status'] is None:
                output['status'] = "success"
        case 201:
            if output['message'] is None:
                output['message'] = "Created"
            if output['status'] is None:
                output['status'] = "success"
        case 400:
            if output['message'] is None:
                output['message'] = "Bad Request"
            if output['status'] is None:
                output['status'] = "error"
        case 401:
            if output['message'] is None:
                output['message'] = "Unauthorized"
            if output['status'] is None:
                output['status'] = "error"
        case 403:
            if output['message'] is None:
                output['message'] = "Forbidden"
            if output['status'] is None:
                output['status'] = "error"
        case 404:
            if output['message'] is None:
                output['message'] = "Not Found"
            if output['status'] is None:
                output['status'] = "error"
        case 500:
            if output['message'] is None:
                output['message'] = "Internal Server Error"
            if output['status'] is None:
                output['status'] = "error"
        case 501:
            if output['message'] is None:
                output['message'] = "Method Not Implemented"
            if output['status'] is None:
                output['status'] = "error"
        case 505:
            if output['message'] is None:
                output['message'] = "Method Not Allowed"
            if output['status'] is None:
                output['status'] = "error"
        case _:
            if output['message'] is None:
                output['message'] = "Internal Server Error"
            if output['status'] is None:
                output['status'] = "error"
            code = 500

    # Update Response
    if errors is not None:
        output['errors'] = errors
    if payload is not None:
        output['payload'] = payload
    if output['status'] is None:
        output['status'] = "unknown"

    # Return Response
    return Response(
        dumps(output),
        code,
        mimetype='application/json'
    )
