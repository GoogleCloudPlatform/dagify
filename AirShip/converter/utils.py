# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import os
import yaml
import pprint


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
    file_path = os.path.abspath(file_path)
    return os.path.isfile(file_path)


def is_directory(folder_path):
    """Checks if a path is a directory.

    Args:
        folder_path (str): The path to the folder.

    Returns:
        bool: True if the path is a directory, False otherwise.
    """
    return os.path.isdir(folder_path)


def directory_exists(folder_path):
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


def read_yaml_to_dict(yaml_file):
    """Loads a YAML file into a dictionary.

    Args:
        yaml_file (str): The path to the YAML file.

    Returns:
        dict: The dictionary representation of the YAML file.
    """
    if yaml_file is None or not file_exists(yaml_file):
        raise FileNotFoundError(
            "AirShip: template file provided is None or does not exist")
        return

    with open(yaml_file, 'r') as file:
        return yaml.safe_load(file)


def display_dict(dict):
    """Pretty prints a dictionary.

    Args:
        dict (dict): The dictionary to print.
    """
    pprint.pprint(dict)
