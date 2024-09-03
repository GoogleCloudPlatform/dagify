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
import pprint
import xml.etree.ElementTree as ET
import json
import yaml
from prettytable import PrettyTable

from .uf import (
    UF,
    UFTask,
    UFTaskVariable,
    UFTaskInCondition,
    UFTaskOutCondition,
    UFTaskShout,
)


def load_source(source_path):
    """ Read the Source File
        Parse into dagify Universial Format
        Output the dagify Universial Format Back to the Class"""
    if source_path is None:
        raise ValueError("dagify: source file cannot be None or Empty")
    if file_exists(source_path) is False:
        raise FileNotFoundError(
            "dagify: source file not found at {}".format(
                source_path))

    root = ET.parse(source_path).getroot()
    uf = parse_universal_format(root)
    return uf


def parse_universal_format(source):
    """Function to parse uf"""
    uf = UF()
    uf = parse_controlm_tree(source, uf)
    return uf


def parse_controlm_tree(root_node, parent):
    """Function to parse control m"""
    for node in root_node:
        match node.tag:
            case "FOLDER" | "SMART_FOLDER":
                # ufFolder = UFFolder()
                # ufFolder.from_controlm_xml(node)
                # parent.add_folder(ufFolder)
                parse_controlm_tree(node, parent)
            case "JOB":
                ufTask = UFTask()
                ufTask.from_controlm_xml(node)
                parent.add_task(ufTask)
                parse_controlm_tree(node, ufTask)
            case "VARIABLE":
                ufTaskVariable = UFTaskVariable()
                ufTaskVariable.from_controlm_xml(node)
                parent.add_variable(ufTaskVariable)
                parse_controlm_tree(node, ufTaskVariable)
            case "INCOND":
                ufTaskInCondition = UFTaskInCondition()
                ufTaskInCondition.from_controlm_xml(node)
                parent.add_in_condition(ufTaskInCondition)
                parse_controlm_tree(node, ufTaskInCondition)
            case "OUTCOND":
                ufTaskOutCondition = UFTaskOutCondition()
                ufTaskOutCondition.from_controlm_xml(node)
                parent.add_out_condition(ufTaskOutCondition)
                parse_controlm_tree(node, ufTaskOutCondition)
            case "SHOUT":
                ufTaskShout = UFTaskShout()
                ufTaskShout.from_controlm_xml(node)
                parent.add_shout(ufTaskShout)
                parse_controlm_tree(node, ufTaskShout)
            case _:
                print("Node: " + node.tag + " is not currently supported.")

    return parent


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
            "dagify: template file provided is None or does not exist")
        return

    with open(yaml_file, 'r') as file:
        return yaml.safe_load(file)


def display_dict(dict):
    """Pretty prints a dictionary.

    Args:
        dict (dict): The dictionary to print.
    """
    pprint.pprint(dict)


def count_yaml_files(directory, case_sensitive=True, recursive=False):
    """
    Counts the number of YAML files (.yaml or .yml) in a directory.

    Args:
        directory (str): The path to the directory to search.
        case_sensitive (bool): Whether the search should be case-sensitive (default: True).
        recursive (bool): Whether to search subdirectories recursively (default: False).

    Returns:
        int: The number of YAML files found.
    """

    count = 0
    for files in os.walk(directory):
        for file in files:
            if (case_sensitive and file.endswith(('.yaml', '.yml'))) or \
               (not case_sensitive and file.lower().endswith(('.yaml', '.yml'))):
                count += 1
        if not recursive:
            break  # Stop after the first level if not recursive

    return count


def generate_table(title, columns, rows):
    """ Function to generate Table with given title, column and row details """
    table = PrettyTable()
    table.title = title
    # Column config
    table.field_names = columns
    for col in columns:
        table.align[col] = "l"
    # Row config
    table.add_rows(rows)
    return table


def generate_report_utils(tables, output_dir, lines=None, warning_line=None):
    """ Function to open a file and write the contents of the report in the file """

    job_table, schedule_table = tables[0], tables[1]
    report_file = f"{output_dir}/Detailed-Report.txt"  # prefix

    with open(report_file, "w") as final_report:
        if lines:
            for line in lines:
                final_report.write(line + '\n')

        final_report.write('\n' + str(job_table) + '\n')

        if warning_line:
            final_report.write('\n' + warning_line + '\n')

        final_report.write('\n' + str(schedule_table) + '\n')


def calculate_percentages(not_converted, converted):
    """Function to calculate the percentages"""
    total = len(not_converted) + len(converted)
    non_converted_percent = round((len(not_converted) / total) * 100, 2)
    converted_percent = round(100 - non_converted_percent, 2)

    return non_converted_percent, converted_percent


def get_tasktype_statistics(source_jt, config_jt):
    """Function to caluculate the percentage conversion"""
    converted_percent = 0
    non_converted_percent = 0

    # Conversion Info
    job_types_converted = list(set(config_jt) & set(source_jt))
    job_types_not_converted = list(set(source_jt) - set(config_jt))

    # Percentages
    non_converted_percent, converted_percent = \
        calculate_percentages(job_types_not_converted, job_types_converted)

    return job_types_converted, job_types_not_converted, converted_percent, non_converted_percent


def get_jobtypes_andcount(source_path):
    """Generic function that calculates the job_types and the count from any input"""
    unique_job_types = []
    job_types_source = []
    job_types_count = 0
    if source_path.endswith('.xml'):
        tree = ET.parse(source_path)
        root = tree.getroot()
        # Find all JOB elements
        job_elements = root.findall('.//JOB')
        # Extract TASKTYPE values and store them in a set to ensure uniqueness
        job_types_source = list({job.get('TASKTYPE') for job in job_elements})
        # Convert all to lowercase for comparision
        job_types_source = [item.lower() for item in job_types_source]
        unique_job_types = list(set(job_types_source))
        job_types_count = len(unique_job_types)
    elif source_path.endswith('config.yaml'):
        with open(source_path, 'r') as file:
            data = yaml.safe_load(file)
        for mapping in data['config']['mappings']:
            job_types_source.append(mapping['job_type'])

        # Convert all to lowercase for comparision
        job_types_source = [item.lower() for item in job_types_source]
        unique_job_types = list(set(job_types_source))
        job_types_count = len(unique_job_types)
    return unique_job_types, job_types_count


def format_table_json(title, columns, rows):
    """Formats table data into a JSON-friendly structure"""

    table_data = {
        "title": title,
        "columns": columns,
        "rows": []
    }

    for row in rows:
        row_dict = {}
        for col_index, value in enumerate(row):
            row_dict[columns[col_index]] = value
        table_data["rows"].append(row_dict)

    return table_data


def generate_json(statistics, job_table_data, schedule_table_data, output_file_path):
    """Creates a JSON file with intro text, table data, and conclusion text"""

    data = {
        "High_Level_Info": statistics,
        "Job_info_table": job_table_data,
        "Schedule_info_table": schedule_table_data
    }
    json_file_path = f"{output_file_path}/report.json"
    with open(json_file_path, "w") as json_file:
        json.dump(data, json_file, indent=2)  # indent for better readability


def get_job_info(file_path):
    """Function to get and return a dictionary of job_name and its task_type"""
    if not file_path.endswith('.xml'):
        raise ValueError(f"Invalid file format: {file_path}. Only XML files are supported.")
    job_info_list = []
    tree = ET.parse(file_path)
    root = tree.getroot()
    # Find all JOB elements
    for job in root.findall('.//JOB'):  # Find all JOB elements
        job_name = job.attrib['JOBNAME']
        task_type = job.attrib['TASKTYPE'].lower()
        job_info_list.append({'job_name': job_name, 'task_type': task_type})
    return job_info_list


def get_job_statistics(job_info_list, config_task_type):
    """Function to calculate and return job_name statistics"""
    unconverted_job_name = [job['job_name'] for job in job_info_list
                            if job['task_type'] not in config_task_type]
    converted_job_name = [job['job_name'] for job in job_info_list
                          if job['task_type'] in config_task_type]
    conv_job_count = len(converted_job_name)
    non_converted_job_percent, converted_job_percent = \
        calculate_percentages(unconverted_job_name, converted_job_name)
    return unconverted_job_name, converted_job_name, \
        non_converted_job_percent, converted_job_percent, conv_job_count


def get_template_name(self, job_type):
    """Function to return template_name for a particular job_type"""
    for mapping in self.config["config"]["mappings"]:
        if mapping["job_type"] == job_type.upper():
            return mapping["template_name"]
    # no match found
    return None


def calculate_cron_schedule(task):
    """Function to calculate cron schedule for a given task"""
    timefrom = task.get_attribute("TIMEFROM")

    if not timefrom:
        return None

    schedule_interval = None
    minute = timefrom[2:]
    hour = timefrom[:2]
    weekdays = task.get_attribute("WEEKDAYS")
    if weekdays:
        day_of_week = ",".join(weekdays.split(","))
    else:
        day_of_week = "*"

    month_abbreviations = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    # Get the list of months that are set to "1"
    months = [i + 1 for i, month in enumerate(month_abbreviations) if task.get_attribute(month) == "1"]
    if months:
        months.sort()
        # Identify consecutive month ranges
        month_ranges = []
        current_range = [months[0]]
        for i in range(1, len(months)):
            if months[i] == current_range[-1] + 1:  # Check for consecutive months
                current_range.append(months[i])
            else:
                month_ranges.append(current_range)  # Start a new range if not consecutive
                current_range = [months[i]]
        month_ranges.append(current_range)  # Add the last range

        month_parts = []
        for r in month_ranges:
            if len(r) == 1:
                month_parts.append(str(r[0]))  # Single month
            else:
                month_parts.append(f"{r[0]}-{r[-1]}")  # Month range

        month_schedule = ",".join(month_parts)
    else:
        month_schedule = "*"

    schedule_interval = [minute, hour, "*", month_schedule, day_of_week]  # Day of month to start is set to "*"
    schedule_interval = " ".join(schedule_interval)
    return schedule_interval


def filter_jobs_by_parameter_in_child(xml_file_path, parameter_name, child_element_name=None):
    """Function to return job_name with a particular paramter"""
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    matching_job_names = []

    for job in root.findall('.//JOB'):
        if child_element_name:
            child_element = job.find(f'./{child_element_name}')
            if child_element is not None and child_element.attrib.get(parameter_name) is not None:
                matching_job_names.append(job.attrib['JOBNAME'])
        else:  # Search within the JOB tag itself
            if job.attrib.get(parameter_name) is not None:
                matching_job_names.append(job.attrib['JOBNAME'])

    return matching_job_names
