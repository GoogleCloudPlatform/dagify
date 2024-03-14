import os
from sqlalchemy import select
from werkzeug.utils import secure_filename
from app.extensions import store
from app.utils.exceptions import ValidationError, NotImplementedError
from app.utils.file_handling import UniqueFilename
from app.models.Conversions import Conversions, conversions_schema, conversion_schema
from app.extensions import db


def create_conversion(file=None, name=None, description=None, **kwargs):
    # Validate file has been provided
    if file is None:
        raise ValidationError("no file provided")
    # Validate conversion name has been provided
    if name is None:
        raise ValidationError("no conversion name provided")
    # Validate upload storage is configured
    if store.get_upload_folder() is None:
        raise ValidationError("server upload storage misconfigured")

    try:
        # Generate Unique Filename
        filename = UniqueFilename(
            secure_filename(file.filename)
        )
        # Save the uploaded file to disk in upload folder
        file.save(
            os.path.join(
                store.get_upload_folder(),
                filename
            )
        )
    except Exception:
        raise

    # Create Conversion Database Record
    conversion = Conversions(
        name=name,
        description=description,
        filename=filename,
    )
    # Add Conversion to the session
    db.session.add(conversion)
    # Commit to database
    db.session.commit()
    # Serialize the Schema
    json_result = conversion_schema.dump(conversion)
    if json_result is None:
        raise Exception("unable to serialize json response")
    # Return JSON Data
    return json_result


def get_conversions():
    # Query database for Conversions
    stmt = select(Conversions)
    conversions = db.session.execute(stmt)
    # Serialize the Schema
    json_result = conversions_schema.dump(conversions)
    if json_result is None:
        raise Exception("unable to serialize json response")
    # Return JSON Data
    return json_result


def get_conversion_by_id(conversion_id=None):
    if conversion_id is None:
        raise ValidationError("no conversion id provided")
    # Query database for Conversions
    stmt = select(Conversions).where(Conversions.id == conversion_id)
    conversion = db.session.execute(stmt)
    # Serialize the Schema
    json_result = conversion_schema.dump(conversion)
    if json_result is None:
        raise Exception("unable to serialize json response")
    # Return JSON Data
    return json_result


def delete_conversion_by_id(conversion_id=None):
    # TODO: Implement
    raise NotImplementedError
    if conversion_id is None:
        raise ValidationError("conversion id required")
    return


def update_conversion_by_id(conversion_id=None):
    # TODO: Implement
    raise NotImplementedError
    if conversion_id is None:
        raise ValidationError("conversion id required")
    return
