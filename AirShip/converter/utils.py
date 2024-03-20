import re
import os

def clean_converter_type(converter_type):
    """Cleans a converter type string by removing all non-alphanumeric characters and converting it to uppercase.

    Args:
        converter_type (str): The converter type to clean.

    Returns:
        str: The cleaned converter type.
    """
    return re.sub("[^A-Za-z0-9]+", "", converter_type).upper()


def file_exists(file_path):
    """Checks if a file exists.

    Args:
        file_path (str): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)


def is_directory(folder_path): 
    """Checks if a path is a directory.

    Args:
        folder_path (str): The path to the folder.

    Returns:
        bool: True if the path is a directory, False otherwise.
    """
    return os.path.isdir(folder_path)


def directory_extist(folder_path):
    """Checks if a folder exists.

    Args:
        folder_path (str): The path to the folder.

    Returns:
        bool: True if the folder exists, False otherwise.
    """
    return os.path.isdir(folder_path)

def create_directory(folder_path):
    """Creates a folder if it does not already exist.

    Args:
        folder_path (str): The path to the folder to create.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)