import json
from flask import request
from marshmallow import Schema, fields, validate, post_load, EXCLUDE
from marshmallow import ValidationError as MarshmallowValidationError
from app.extensions import store
from app.utils.exceptions import ValidationError, NotImplementedError
from app.api.v1 import bp
from app.api.utils import HandleResponse
from app.utils.file_handling import AllowedFileType
from app.core.handlers import conversions as c


@bp.route('/conversions', methods=['GET', 'POST'])
def api_conversions():
    # Get All Conversions 
    if request.method == 'GET':
        try:
            conversions = c.get_conversions()
            # Success return HTTP 200
            return HandleResponse(code=200,
                                  message='conversions loaded',
                                  payload=conversions
                                  )
        except Exception as e:
            return HandleResponse(code=500,
                                  message="unable to load conversions",
                                  errors={'conversions': str(e)}
                                  )
        

    # Create New Conversion
    if request.method == 'POST':
        # Create Request Body Class Object
        class RequestBody():
            def __init__(self, name=None, description=None) -> None:
                self.name = name
                self.description = description

        # Create Request Body Class Object Schema
        class RequestBodySchema(Schema):
            name = fields.Str(required=True,
                              validate=validate.Length(min=5, max=200))
            description = fields.Str(required=False,
                                     validate=validate.Length(max=500))

            class Meta:
                # Exclude unknown fields in the deserialized output
                unknown = EXCLUDE

            @post_load
            def make_request(self, data, **kwargs)->RequestBody:
                return RequestBody(**data)

        # Validate Request Details
        # Check file has been provided in HTTP Request
        if 'file' not in request.files:
            return HandleResponse(code=400,
                                  message='No file part in the request',
                                  errors={'file': 'no file provided'})
        # Get file from HTTP Request
        file = request.files['file']
        # Empty file, with no filename
        if file.filename == '':
            return HandleResponse(code=400,
                                  message='No file selected for uploading',
                                  errors={'file': 'no file provided'})
        # Check if the file extension is allowed
        try:
            if not AllowedFileType(file.filename):
                return HandleResponse(code=400,
                                      message='File type not allowed',
                                      errors={'filetype': 'filetype is not allowed to be uploaded'})
        except ValidationError as e:
            return HandleResponse(code=400, message=str(e.msg))
        # Check Upload Folder Exists
        if store.get_upload_folder() is None:
            return HandleResponse(code=500,
                                  message='server upload storage misconfigured',
                                  errors={'storage': 'not able to validate upload directories existence'})

        # Validate and deserialize input
        if request.form.get('data') is None:
            return HandleResponse(code=400,
                                  message='no input data provided',
                                  errors={'request': 'the json body is empty in the request'})


        json_data = json.loads(request.form.get('data'))
        if not json_data:
            return HandleResponse(code=400,
                                  message='no input data provided',
                                  errors={'request': 'the json body is empty in the request'})

        # Validate and deserialize JSON input
        try:
            requestBody = RequestBodySchema().load(
                json_data,
                partial=True,
                unknown=EXCLUDE
                )
        except MarshmallowValidationError as err:
            return HandleResponse(code=400,
                                  message='request data invalid',
                                  errors=err.messages_dict)

        # Validated; Attempt to Create Conversion
        try:
            conversion = c.create_conversion(
                file=file,
                name=requestBody.name,
                description=requestBody.description
            )
            # Success Return HTTP 201
            return HandleResponse(code=201,
                                  message='conversion successfully created',
                                  payload=conversion
                                  )
        except Exception as e:
            # Error Return HTTP 500
            return HandleResponse(code=500,
                                  message="unable to create conversion",
                                  errors={'conversions': str(e)}
                                  )
           
    # Unknown Error return HTTP 500
    return HandleResponse(code=500,
                          message="unexpected error",
                          errors={'conversions': []}
                          )



@bp.route('/conversions/<conversion_id>', methods=['GET', 'POST', 'DELETE'])
def api_conversion(conversion_id=None):
    if conversion_id is None:
        return HandleResponse(code=400)
    # Get Conversion by ID
    if request.method == 'GET':
        try:
            conversion = c.get_conversion_by_id(
                conversion_id=conversion_id
            )
            # Success Return HTTP 201
            return HandleResponse(code=200,
                                  message='conversions loaded',
                                  payload=conversion
                                  )
        except NotImplementedError as e:
            # Implementation Error Return HTTP 501
            return HandleResponse(code=501,
                                  message=str(e.msg)
                                  )
        except Exception as e:
            # Error Return HTTP 500
            return HandleResponse(code=500,
                                  message="unable to load conversion",
                                  errors={'conversions': str(e)}
                                  )
        except ValidationError as e:
            return HandleResponse(code=400,
                                  message="validation error, unable to load conversions",
                                  errors={'conversions': str(e.msg)}
                                  )
            
    # Update Conversion by ID
    if request.method == 'POST':
        try:
            c.update_conversion_by_id(conversion_id=conversion_id)
        except NotImplementedError as e:
            # Implementation Error Return HTTP 501
            return HandleResponse(code=501,
                                  message=str(e.msg)
                                  )
        except ValidationError as e:
            # Validation Error Return HTTP 400
            return HandleResponse(code=400, 
                                  message="validation error, unable to update conversion",
                                  errors={'conversions': str(e.msg)}
                                  )
        except Exception as e:
            # Error Return HTTP 500
            return HandleResponse(code=500,
                                  message="unable to update conversion",
                                  errors={'conversions': str(e)}
                                  )

    # Delete Conversion by ID
    if request.method == 'DELETE':
        try:
            c.delete_conversion_by_id(conversion_id=conversion_id)
        except NotImplementedError as e:
            # Implementation Error Return HTTP 501
            return HandleResponse(code=501,
                                  message=str(e.msg)
                                  )
        except ValidationError as e:
            # Validation Error Return HTTP 400
            return HandleResponse(code=400, 
                                  message="validation error, unable to delete conversion",
                                  errors={'conversions': str(e.msg)}
                                  )
        except Exception as e:
            # Error Return HTTP 500
            return HandleResponse(code=500,
                                  message="unable to delete conversion",
                                  errors={'conversions': str(e)}
                                  )
        
    # Unknown Error return HTTP 500
    return HandleResponse(code=500,
                          message="unexpected error",
                          errors={'conversions': []}
                          )