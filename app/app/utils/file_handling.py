import pathlib
import uuid
from datetime import datetime
from app.utils.exceptions import ValidationError


def AllowedFileExtensions():
    """
    This function returns a set of allowed file extensions.

    Returns:
        set: A set of allowed file extensions.
    """
    return set(['xml'])


def AllowedFileType(filename):
    """
    This function checks if a filename has an allowed file extension.

    Args:
        filename (str): The filename to check.

    Returns:
        bool: True if the filename has an allowed file extension, False
        otherwise.
    """
    if filename is None:
        raise ValidationError("filename can not be empty")
    return '.' \
        in filename \
        and filename.rsplit('.', 1)[1].lower() \
        in AllowedFileExtensions()


def GetFileExt(filename):
    return pathlib.Path(filename).suffix


def UniqueFilename(filename):
    return datetime.now().strftime("%Y%m%d%H%M%S") +\
        '_' + \
        str(uuid.uuid4())[0:6] \
        + GetFileExt(filename)
