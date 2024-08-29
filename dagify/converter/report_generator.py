"""Module providing function to manipulate yaml files"""
import yaml
from .utils import (
    is_directory,
    generate_report,
    get_jobtypes_andcount,
    generate_json,
    format_table_data,
    get_job_info,
    get_tasktype_statistics,
    get_job_statistics,
    filter_jobs_by_parameter_in_child
)


class Report():
    """Report generating module """

    def __init__(
        self,
        source_path=None,
        output_path=None,
        templates_path="./templates",
        config_file="./config.yaml",
    ):
        self.config_file = config_file
        self.config = {}
        self.templates = {}
        self.source_path = source_path
        self.output_path = output_path
        self.templates_path = templates_path

        # Run the Proccess
        self.generate_report()

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
        non_converted_job_percent, converted_job_percent = \
            get_job_statistics(job_info,config_job_types)
        # Statistics Info parameters
        job_types_converted, job_types_not_converted, converted_percentage, \
            non_converted_percentage = \
            get_tasktype_statistics(job_types_source, config_job_types)  
        # Get Manual Intervention Job_Name Info
        manual_job_names = filter_jobs_by_parameter_in_child(self.source_path,"CONFIRM")

        # Table Info
        statistics = [
            f"Percentage of Jobtypes converted: {converted_percentage}%",
            f"Percentage of Jobtypes not converted: {non_converted_percentage}%",
            f"Percentage of Jobs converted: {non_converted_job_percent}%",
            f"Percentage of Jobs not converted: {converted_job_percent}%",
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
        formatted_table_data = format_table_data(title, columns, rows)

        warning_line = "NOTE: \n \
            1. If the job_type is not defined in the config.yaml or \
            if the job_type does not have a matching template defined,it would be by default converted into a DUMMYOPERATOR\n \
            2. Jobs_Requiring_Manual_Approval - indicates that the job has CONFIRM PARAMTER defined in job, \
                meaning the workflow has to be changed for manual approval for these jobs/job"

        generate_json(statistics, formatted_table_data, self.output_path)
        generate_report(statistics, title, columns, rows, warning_line, self.output_path)
