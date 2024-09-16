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

import xml.etree.ElementTree as ET
import yaml
from .utils import (
    is_directory,
    generate_report_utils,
    get_jobtypes_andcount,
    generate_json,
    format_table_json,
    get_job_info,
    get_tasktype_statistics,
    get_job_statistics,
    filter_jobs_by_parameter_in_child,
    calculate_cron_schedule,
    directory_exists,
    create_directory,
    generate_table,
    load_source
)


class Report():
    """Report generating module """

    def __init__(
        self,
        source_path=None,
        output_path=None,
        templates_path="./templates",
        config_file="./config.yaml",
        dag_divider="PARENT_FOLDER"
    ):
        self.config_file = config_file
        self.config = {}
        self.templates = {}
        self.source_path = source_path
        source_xml_name = self.source_path.split("/")[-1].split(".")[0]
        self.output_path = f"{output_path}/{source_xml_name}"
        self.templates_path = templates_path
        self.dag_divider = dag_divider
        self.uf = load_source(self.source_path)
        # Run the Proccess
        self.write_report()

    def check_schedules(self, dag_divider):
        """Function to check schedules exist and generate reprot table"""
        title = "Updated Job Schedules"
        columns = ["JOB NAME", "DAG DIVIDER", "SCHEDULE CHANGE", "ORIGINAL SCHEDULE", "DAG SCHEDULE"]
        rows = []
        prev_divider = None
        dag_schedule = None
        universal_format = self.uf
        tasks = universal_format.get_tasks()
        for tIdx, task in enumerate(tasks):
            current_divider = task.get_attribute(dag_divider)

            if not prev_divider:
                prev_divider = current_divider

            if prev_divider and prev_divider != current_divider:  # New DAG and schedule will be created
                prev_divider = current_divider
                dag_schedule = None  # reset schedule to empty

            if not dag_schedule:  # first schedule for this dag , defined for all jobs with this divider
                dag_schedule = calculate_cron_schedule(task)
                if not dag_schedule:
                    dag_schedule = "@daily"

            if current_divider == prev_divider: # Tabulate if schedule varies or not for a job under same dag_divider 
                current_schedule = calculate_cron_schedule(task)
                job_name = task.get_attribute("JOBNAME")
                if current_schedule != dag_schedule:
                    rows.append((job_name, current_divider, "YES", current_schedule, dag_schedule))
                else:
                    rows.append((job_name, current_divider, "NO", current_schedule, dag_schedule))

        return title, columns, rows

    def generate_report(self):
        """Function that generates the json and txt report"""
        templates_to_validate = []
        # Config_File_Info parameters
        config_job_types = []
        config_job_types_count = 0
        # Source_file_Info parameters
        source_files_count = 1
        source_file_info = []
        job_types_source = []
        job_types_source_count = 0

        # Get the Job_types from config_file
        config_job_types, config_job_types_count = get_jobtypes_andcount(self.config_file)

        # Get the Job_types from source xml
        if is_directory(self.source_path) is False:
            source_file_info.append(self.source_path.split("/")[-1])
            job_types_source, job_types_source_count = get_jobtypes_andcount(self.source_path)

        # Get templates INFO
        with open(self.config_file, encoding="utf-8") as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise exc
        for idx, config in enumerate(self.config["config"]["mappings"]):
            self.config["config"]["mappings"][idx]["job_type"] = \
                self.config["config"]["mappings"][idx]["job_type"].upper()
            templates_to_validate.append(self.config["config"]["mappings"][idx]["template_name"])

        # Get job related info
        job_info = get_job_info(self.source_path)
        unconverted_job_name, converted_job_name, \
            non_converted_job_percent, converted_job_percent, conv_job_count = \
            get_job_statistics(job_info, config_job_types)
        # Statistics Info parameters
        job_types_converted, job_types_not_converted, converted_percentage, \
            non_converted_percentage = \
            get_tasktype_statistics(job_types_source, config_job_types)
        # Get Manual Intervention Job_Name Info
        manual_job_names = filter_jobs_by_parameter_in_child(self.source_path, "CONFIRM")

        # Table Info
        statistics = [
            f"Jobtypes converted: {len(job_types_converted)}/{len(job_types_source)}",
            f"Percentage of Jobtypes converted: {converted_percentage}%",
            f"Percentage of Jobtypes not converted: {non_converted_percentage}%",
            f"Jobs converted: {conv_job_count}/{len(job_info)}",
            f"Percentage of Jobs converted: {converted_job_percent}%",
            f"Percentage of Jobs not converted: {non_converted_job_percent}%",
        ]
        title = "DAGIFY REPORT"
        columns = ["TASK", "INFO", "COUNT"]
        rows = [
            ["Source_files", source_file_info, source_files_count],
            ["Source_File_Job_Types", job_types_source, job_types_source_count],
            ["Config_File_Job_Types", config_job_types, config_job_types_count],
            ["Job_Types_Converted", job_types_converted, len(job_types_converted)],
            ["Job_types_Not_Converted", job_types_not_converted, len(job_types_not_converted)],
            ["Jobs_Converted", converted_job_name, len(converted_job_name)],
            ["Jobs_Not_Converted", unconverted_job_name, len(unconverted_job_name)],
            ["Jobs_Requiring_Manual_Approval", manual_job_names, len(manual_job_names)],
            ["Templates_Validated", templates_to_validate, len(templates_to_validate)]
        ]

        warning_line = "NOTE: \n \
       1. If the job_type is not defined in the config.yaml or if the job_type does not have a matching template defined,it would be by default converted into a DUMMYOPERATOR\n \
       2. Jobs_Requiring_Manual_Approval - indicates that the job has CONFIRM PARAMTER defined in job, meaning the workflow has to be changed for manual approval for these jobs/job"

        return title, columns, rows, statistics, warning_line

    def write_report(self):
        """Function that generates the json and txt report"""
        report_tables = []
        if not directory_exists(self.output_path):
            create_directory(self.output_path)

        job_title, job_columns, job_rows, job_statistics, job_warning = self.generate_report()
        job_conversion_table = generate_table(job_title, job_columns, job_rows)

        schedules_title, schedules_columns, schedules_rows = self.check_schedules(dag_divider=self.dag_divider)
        schedule_table = generate_table(schedules_title, schedules_columns, schedules_rows)

        report_tables.append(job_conversion_table)
        report_tables.append(schedule_table)
        generate_report_utils(report_tables, self.output_path, job_statistics, job_warning)
        # json_generation
        formatted_job_table_data = format_table_json(job_title, job_columns, job_rows)
        formatted_schedule_table_data = format_table_json(schedules_title, schedules_columns, schedules_rows)
        generate_json(job_statistics, formatted_job_table_data, formatted_schedule_table_data, self.output_path)
