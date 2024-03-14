from flask import request
from app.utils.exceptions import ValidationError, NotImplementedError
from app.api.v1 import bp
from app.api.utils import HandleResponse
from app.core.handlers import analyses as a


@bp.route('/conversions/<conversion_id>/analyses', methods=['GET', 'POST'])
def api_analyses(conversion_id=None):
    if conversion_id is None:
        return HandleResponse(400)

    # Get Analyses
    if request.method == 'GET':
        try:
            a.get_analyses_by_conversion_id(conversion_id=conversion_id)
        except NotImplementedError as e:
            # Implementation Error Return HTTP 501
            return HandleResponse(code=501,
                                  message=str(e.msg)
                                  )
        except ValidationError as e:
            # Validation Error Return HTTP 400
            return HandleResponse(
                code=400,
                message="validation error, unable to load analyses",
                errors={
                    'analyses': str(
                        e.msg)})
        except Exception as e:
            # Error Return HTTP 500
            return HandleResponse(code=500,
                                  message="unable to load analyses",
                                  errors={'analyses': str(e)}
                                  )

    # Create Analyses
    if request.method == 'POST':
        try:
            a.create_analyses()
        except NotImplementedError as e:
            # Implementation Error Return HTTP 501
            return HandleResponse(code=501,
                                  message=str(e.msg)
                                  )
        except ValidationError as e:
            # Validation Error Return HTTP 400
            return HandleResponse(
                code=400,
                message="validation error, unable to create analyses",
                errors={
                    'analyses': str(
                        e.msg)})
        except Exception as e:
            # Error Return HTTP 500
            return HandleResponse(code=500,
                                  message="unable to create analyses",
                                  errors={'analyses': str(e)}
                                  )

    # Unknown Error return HTTP 500
    return HandleResponse(code=500,
                          message="unexpected error",
                          errors={'analyses': []}
                          )


@bp.route('/conversions/<conversion_id>/analyses/<analyses_id>',
          methods=['GET', 'DELETE'])
def api_analysis(conversion_id=None, analyses_id=None):
    if conversion_id is None:
        return HandleResponse(400)
    if analyses_id is None:
        return HandleResponse(400)

    # Get Analyses by ID
    if request.method == 'GET':
        try:
            a.get_analyses_by_id(analyses_id=analyses_id)
        except NotImplementedError as e:
            # Implementation Error Return HTTP 501
            return HandleResponse(code=501,
                                  message=str(e.msg)
                                  )
        except ValidationError as e:
            # Validation Error Return HTTP 400
            return HandleResponse(
                code=400,
                message="validation error, unable to load analyses",
                errors={
                    'analyses': str(
                        e.msg)})
        except Exception as e:
            # Error Return HTTP 500
            return HandleResponse(code=500,
                                  message="unable to load analyses",
                                  errors={'analyses': str(e)}
                                  )
        # Unknown Error return HTTP 500
        return HandleResponse(code=500,
                              message="unexpected error",
                              errors={'analyses': []}
                              )

    # Delete Analyses by ID
    if request.method == 'DELETE':
        try:
            a.delete_analyses_by_id(analyses_id=analyses_id)
        except NotImplementedError as e:
            # Implementation Error Return HTTP 501
            return HandleResponse(code=501,
                                  message=str(e.msg)
                                  )
        except ValidationError as e:
            # Validation Error Return HTTP 400
            return HandleResponse(
                code=400,
                message="validation error, unable to delete analyses",
                errors={
                    'analyses': str(
                        e.msg)})
        except Exception as e:
            # Error Return HTTP 500
            return HandleResponse(code=500,
                                  message="unable to delete analyses",
                                  errors={'analyses': str(e)}
                                  )
        # Unknown Error return HTTP 500
        return HandleResponse(code=500,
                              message="unexpected error",
                              errors={'analyses': []}
                              )
