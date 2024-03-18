import re

def clean_converter_type(converter_type):
    """Cleans a converter type string by removing all non-alphanumeric characters and converting it to uppercase.

    Args:
        converter_type (str): The converter type to clean.

    Returns:
        str: The cleaned converter type.
    """
    return re.sub("[^A-Za-z0-9]+", "", converter_type).upper()
